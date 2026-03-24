"""
Simple local web server for the Quiz app.
Usage:  python server.py          (default port 8000)
        python server.py 5000     (custom port)
"""

import http.server
import socketserver
import webbrowser
import sys
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

# Serve from the directory this script lives in
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler that suppresses per-request log noise."""

    def log_message(self, fmt, *args):
        # Only show errors (4xx / 5xx) and the startup banner
        code = args[1] if len(args) > 1 else ""
        try:
            if int(code) >= 400:
                super().log_message(fmt, *args)
        except (ValueError, TypeError):
            pass


with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
    url = f"http://localhost:{PORT}"
    print("=" * 52)
    print(f"  Quiz App server running at {url}")
    print(f"  Serving files from: {os.getcwd()}")
    print("  Press Ctrl+C to stop.")
    print("=" * 52)
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
