#!/usr/bin/env python3
"""Validate all question JSON files against their schemas."""

import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: 'jsonschema' package is not installed. Run: pip install jsonschema")
    sys.exit(1)

QUESTIONS_DIR = Path(__file__).parent / "questions"
QUESTION_SCHEMA_FILE = QUESTIONS_DIR / "question-schema.json"
MANIFEST_SCHEMA_FILE = QUESTIONS_DIR / "manifest-schema.json"
MANIFEST_FILE = QUESTIONS_DIR / "manifest.json"

SKIP_FILES = {"manifest.json", "question-schema.json", "manifest-schema.json"}


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_file(data: object, schema: dict, filepath: Path) -> list[str]:
    errors = []
    validator = jsonschema.Draft7Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        location = " -> ".join(str(p) for p in error.absolute_path) or "root"
        errors.append(f"  [{location}] {error.message}")
    return errors


def main() -> int:
    question_schema = load_json(QUESTION_SCHEMA_FILE)
    manifest_schema = load_json(MANIFEST_SCHEMA_FILE)

    failed = 0
    passed = 0

    # Validate manifest
    print(f"Validating {MANIFEST_FILE.name} ...")
    manifest_data = load_json(MANIFEST_FILE)
    errors = validate_file(manifest_data, manifest_schema, MANIFEST_FILE)
    if errors:
        print(f"  FAIL: {MANIFEST_FILE.name}")
        for e in errors:
            print(e)
        failed += 1
    else:
        print(f"  PASS: {MANIFEST_FILE.name}")
        passed += 1

    # Collect question files from manifest + any extra .json files on disk
    manifest_files = set(manifest_data.get("files", []))
    disk_files = {
        f.name for f in QUESTIONS_DIR.glob("*.json") if f.name not in SKIP_FILES
    }

    # Warn about files on disk not listed in manifest
    unlisted = disk_files - manifest_files
    for name in sorted(unlisted):
        print(f"  WARNING: '{name}' exists on disk but is not listed in manifest.json")

    # Warn about files listed in manifest but missing from disk
    missing = manifest_files - disk_files
    for name in sorted(missing):
        print(f"  WARNING: '{name}' is listed in manifest.json but does not exist on disk")
        failed += 1

    # Validate each question file
    for filename in sorted(manifest_files & disk_files):
        filepath = QUESTIONS_DIR / filename
        print(f"Validating {filename} ...")
        data = load_json(filepath)
        errors = validate_file(data, question_schema, filepath)
        if errors:
            print(f"  FAIL: {filename}")
            for e in errors:
                print(e)
            failed += 1
        else:
            print(f"  PASS: {filename} ({len(data)} questions)")
            passed += 1

    print()
    print(f"Results: {passed} passed, {failed} failed")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
