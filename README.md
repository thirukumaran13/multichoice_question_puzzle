# 🧠 Quiz Challenge!

A fully self-contained, browser-based multiple-choice quiz app. No frameworks, no build step — just a single `index.html` and a folder of JSON question files.

---

## 📖 Table of Contents

1. [What Is This?](#-what-is-this)
2. [What You Need](#-what-you-need)
3. [Accessing via GitHub Pages](#-accessing-via-github-pages-easiest--no-setup-required)
4. [Running Locally](#-running-locally-for-custom-question-sets)
5. [Taking a Quiz](#-taking-a-quiz)
6. [Quiz Setup (Filters & Options)](#%EF%B8%8F-quiz-setup-filters--options)
7. [Creating Your Own Questions](#-creating-your-own-questions)
   - [Using the Quiz Creator (Recommended)](#option-a-using-the-quiz-creator-recommended-for-beginners)
   - [Editing JSON directly](#option-b-editing-json-directly-advanced)
8. [Adding an Image to a Question](#-adding-an-image-to-a-question)
9. [Adding Math / Equations](#-adding-math--equations)
10. [Printing a Quiz](#%EF%B8%8F-printing-a-quiz)
11. [Feature Overview](#-feature-overview)
12. [JSON Field Reference](#-json-field-reference)
13. [Troubleshooting](#-troubleshooting)

---

## 💡 What Is This?

Quiz Challenge is a **browser-based quiz app** that runs entirely on your computer — no internet required after the first load. You create question files and open the quiz in any browser.

There are two HTML pages:

| File | Needs web server? | Purpose |
|---|---|---|
| `index.html` | ✅ Yes | **The quiz player** — students take quizzes here |
| `quiz-creator.html` | ❌ No | **The quiz creator** — teachers/authors build question sets; open it directly in a browser |

---

## 🛠 What You Need

- A modern web browser (Chrome, Edge, Firefox, Safari)
- **Python 3** — only needed to run the **quiz player locally**. Not needed to use GitHub Pages or the Quiz Creator.
  - [Download Python 3](https://www.python.org/downloads/) — on Windows, tick "Add Python to PATH" during installation

> ⚠️ **Important:** `index.html` (the quiz player) **cannot** be opened by double-clicking. It must be served through the local web server because it loads question files in the background.
>
> ✅ `quiz-creator.html` (the question editor) **can** be opened directly by double-clicking — no server required.

---

## 🌐 Accessing via GitHub Pages (Easiest — No Setup Required)

The app is hosted publicly on GitHub Pages. No installation or server needed.

| Page | URL |
|---|---|
| **Quiz Player** | [thirukumaran13.github.io/multichoice_question_puzzle/](https://thirukumaran13.github.io/multichoice_question_puzzle/) |
| **Quiz Creator** | [thirukumaran13.github.io/multichoice_question_puzzle/quiz-creator.html](https://thirukumaran13.github.io/multichoice_question_puzzle/quiz-creator.html) |

> **Note:** Question sets on the hosted version are the ones included in the repository. To use your own questions, run the app locally (see below) or add your JSON files to the `questions/` folder and push to the repo.

---

## 🚀 Running Locally (for custom question sets)

### On Windows

1. Open the `multichoice_question_puzzle` folder
2. Double-click **`start_server.bat`**
3. A black terminal window will appear — leave it open
4. Open your browser and go to: **http://localhost:8000**

### On Mac / Linux

1. Open a terminal
2. Navigate to the project folder:
   ```bash
   cd path/to/multichoice_question_puzzle
   ```
3. Start the server:
   ```bash
   python3 server.py
   ```
4. Open your browser and go to: **http://localhost:8000**

### Using a different port

```bash
python server.py 5000      # starts on http://localhost:5000
```

### Stopping the server

Close the terminal window (or press `Ctrl+C` in it).

---

## 🎮 Taking a Quiz

Once the app is open in your browser:

1. **Set up your profile** *(optional)*
   - Click the ⚙️ gear icon (top-right corner)
   - Go to **My Profile** — enter your name, grade, and school
   - Click **💾 Save & Close**
   - Your name will appear on results and printed sheets

2. **Configure the quiz** *(optional)*
   - Click ⚙️ → **Quiz Setup** to filter questions by subject, chapter, category, or difficulty
   - See [Quiz Setup](#%EF%B8%8F-quiz-setup-filters--options) for details

3. **Start the quiz**
   - Click **Start Quiz!**

4. **Answer questions**
   - Click any answer choice
   - In *Immediately* mode: the correct answer is revealed right away
   - In *End of Quiz* mode: you can change your answer and navigate freely before submitting

5. **View results**
   - Your score, accuracy, and time are shown at the end
   - Click **📋 Review Answers** to see every question with correct/wrong highlights

### Quiz Controls

| Button | What it does |
|---|---|
| **⏭ Skip** | Skip the current question (comes back to it later) |
| **✔ Submit Answer** | Confirm your selected answer (End of Quiz mode) |
| **Next →** | Advance to the next question |
| **🏁 End Quiz** | Stop early and go straight to results |
| **Question map** | Click any numbered tile to jump directly to that question |

---

## ⚙️ Quiz Setup (Filters & Options)

Open **⚙️ → Quiz Setup** to customise the quiz before starting.

### Filters

Questions can be tagged with up to four dimensions. Each appears as a filter:

| Filter | What it selects |
|---|---|
| 📚 **Subjects** | Which question file(s) to include (one subject = one JSON file) |
| 📖 **Chapters** | Narrow to specific chapters within a subject |
| 🏷️ **Category** | E.g. Recall / Application / HOTS |
| 📊 **Complexity** | Easy / Medium / Hard — or *(None)* for untagged questions |

- **All tags checked** = include everything (default)
- **Uncheck a tag** to exclude those questions
- The **question count badge** at the bottom updates live as you adjust filters
- Each tag also has a **Max** field to limit how many questions come from that tag

### Question Limits

| Setting | What it does |
|---|---|
| **Max Total** | Cap the total number of questions per session |
| **Per-tag Max** | Limit questions from any individual chapter, category, etc. |

### Result Display

| Mode | How it works |
|---|---|
| 🔍 **Immediately** | The correct answer lights up as soon as you click a choice |
| 🏁 **End of Quiz** | All answers are hidden until you finish — you can re-answer and navigate freely |

### Timed Quiz

Toggle **⏱️ Timed Quiz** on to add a countdown:

| Mode | How it works |
|---|---|
| ⏰ **Per Question** | Each question has its own countdown based on complexity (Easy: 10s, Medium: 20s, Hard: 30s). Time runs out → question is auto-skipped. |
| ⏳ **Total Quiz** | One shared countdown for the whole quiz, set in minutes |

---

## ✏️ Creating Your Own Questions

You have two options: use the **visual Quiz Creator** (easier) or edit a **JSON file** directly (faster for bulk edits).

---

### Option A: Using the Quiz Creator (Recommended for Beginners)

**Simply double-click `quiz-creator.html`** — no server needed. It opens directly in your browser as a local file.

#### Step 1 — Write your question

Type (or paste) the question text in the **Question** field. The toolbar lets you:
- Make text **Bold**, *Italic*, Underlined, ~~Strikethrough~~
- Add inline code, bullet lists, numbered lists, blockquotes
- Insert **math equations** (∑ button — see [Adding Math](#-adding-math--equations))
- Insert **images** (🖼 button — see [Adding Images](#-adding-an-image-to-a-question))

> **Tip:** Click **📝 Raw HTML** to switch to raw HTML editing mode if you prefer to type HTML directly.

#### Step 2 — Add answer choices

Each choice has its own text editor. The **radio button** on the left marks the correct answer.

- Click **＋** to add more choices (up to 6)
- Click the **🗑 bin** icon to remove a choice
- Make sure exactly **one** radio button is selected

#### Step 3 — Fill in optional tags *(recommended)*

| Field | Example | Purpose |
|---|---|---|
| **Chapter / Topic** | `Algebra`, `World War II` | Groups questions for filtering |
| **Category** | `Recall`, `Application`, `HOTS` | Type of cognitive skill |
| **Complexity** | `Low`, `Medium`, `Hard` | Controls the per-question timer |
| **Duration override** | `45` | Custom timer in seconds (overrides complexity default) |
| **Reason** | `Oxytocin triggers uterine contractions.` | Explanation shown to the student after they answer |

#### Step 4 — Save the question

Click **✔ Save Question**. The question appears in the list below the form. You can:
- Click the **✏️ edit** icon to revise a question
- Click the **🗑 delete** icon to remove it
- **Drag** a question row to reorder

#### Step 5 — Download the JSON file

Click **⬇️ Download JSON**. A file like `questions.json` will be saved to your Downloads folder.

#### Step 6 — Put it in the right place

1. Move the downloaded `.json` file into the `questions/` folder
2. Open `questions/manifest.json` and add the filename:

```json
{
  "files": [
    "general.json",
    "my_new_quiz.json"
  ]
}
```

3. Refresh **http://localhost:8000** — your new questions will load automatically

---

### Option B: Editing JSON Directly (Advanced)

Each question file is a plain `.json` file — a list of question objects:

```json
[
  {
    "question": "What is the capital of France?",
    "choices": ["Paris", "London", "Berlin", "Madrid"],
    "answer": 0,
    "chapter": "European Geography",
    "category": "Recall",
    "complexity": "low",
    "reason": "Paris has been the capital of France since the 10th century."
  },
  {
    "question": "Which planet is closest to the Sun?",
    "choices": ["Venus", "Mercury", "Earth", "Mars"],
    "answer": 1,
    "chapter": "Solar System",
    "category": "Recall",
    "complexity": "low"
  }
]
```

**Key rules:**
- `"answer"` is the **0-based index** of the correct choice (0 = first choice, 1 = second, etc.)
- If you omit `"answer"`, the first choice (`0`) is assumed correct
- Choices are **shuffled randomly** at runtime, so the order in your file doesn't matter to the player
- A good habit: always put the correct answer at index 0 and omit the `"answer"` field entirely

#### Creating a new question file

1. Create a file like `questions/history.json`
2. Add your questions in the format above
3. Add the filename to `questions/manifest.json`
4. Refresh the browser

---

## 🖼 Adding an Image to a Question

### Via Quiz Creator

1. Place your cursor in the question or choice text
2. Click the **🖼** image button in the toolbar
3. Enter the image URL or a relative path (e.g. `questions/images/diagram.png`)
4. Optionally set alt text and width
5. Click **Insert**

### Via JSON (raw)

**Option 1 — Object format (recommended):** Use a `{text, img}` object for `question` or any choice:

```json
{
  "question": {
    "text": "What structure is shown in the diagram?",
    "img": "questions/images/cell.png"
  },
  "choices": ["Animal cell", "Plant cell", "Bacteria", "Fungi"],
  "answer": 1
}
```

**Option 2 — Inline `<img>` tag:** Embed an image directly inside the HTML string:

```json
{
  "question": "What structure is shown?<br><img src=\"questions/images/cell.png\" alt=\"Cell diagram\" style=\"max-width:300px\" />",
  "choices": ["Animal cell", "Plant cell", "Bacteria", "Fungi"],
  "answer": 1
}
```

**Image storage tip:** Create a `questions/images/` folder and keep all your images there. Reference them with relative paths like `questions/images/filename.png`.

---

## � JSON Field Reference

| Field | Required | Type | Description |
|---|---|---|---|
| `question` | ✅ | HTML string **or** `{text, img}` object | The question text. Supports all HTML tags and `<latex>…</latex>` for math. Use the object form `{"text": "…", "img": "path/to/img.jpg"}` to attach a standalone image below the question text. |
| `choices` | ✅ | Array of HTML strings or `{text, img}` objects | 2–6 answer options. Same rich content support as `question`. Each choice can be a plain string or `{"text": "…", "img": "…"}`. |
| `answer` | ✗ | Number (0-based) | Index of the correct choice. Defaults to `0` if omitted. |
| `chapter` | ✗ | String | Groups questions under a chapter/topic for filtering. |
| `category` | ✗ | String | e.g. `Recall`, `Application`, `HOTS` |
| `complexity` | ✗ | `low` / `medium` / `hard` | Controls the per-question timer (10s / 20s / 30s). |
| `duration` | ✗ | Number (seconds) | Custom per-question timer — overrides the complexity default. |
| `reason` | ✗ | HTML string | Explanation shown to the student after the answer is revealed (in the feedback banner and on the Review screen). Supports the same HTML & LaTeX as `question`. |

### Supported HTML tags inside `question` and `choices`

| Content type | Tags |
|---|---|
| Text formatting | `<strong>`, `<em>`, `<u>`, `<s>`, `<sup>`, `<sub>` |
| Code | `<code>`, `<pre><code>…</code></pre>` |
| Images | `<img src="…" alt="…">`, `<figure><img…><figcaption>…</figcaption></figure>` |
| Tables | `<table>`, `<tr>`, `<th>`, `<td>` |
| Lists | `<ul>/<ol>` with `<li>` |
| Blockquote | `<blockquote>` |
| Math | `<latex>x^2</latex>` (inline), `<latex display>\frac{a}{b}</latex>` (block) |
| Other | `<br>`, `<hr>`, `<p>` |

### Per-question timer defaults (complexity-based)

| Complexity | Default time |
|---|---|
| `low` (Easy) | 10 s |
| `medium` | 20 s |
| `hard` | 30 s |
| `duration` field set | Overrides all of the above |

---

## 📁 Project Structure

```
multichoice_question_puzzle/
├── index.html              # Quiz player — HTML + CSS + JS in one file
├── quiz-creator.html       # Visual question editor
├── server.py               # Simple Python HTTP server
├── start_server.bat        # Windows launcher for server.py
└── questions/
    ├── manifest.json       # Lists which JSON files to load
    ├── general.json        # General knowledge question set
    ├── X Biology.json      # Class X Biology question set
    └── images/             # Images referenced by questions
```

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| **"Could not load questions"** error | You opened `index.html` directly as a file. Use the local server instead (`start_server.bat` or `python server.py`). |
| **New questions not showing up** | Make sure the filename is listed in `questions/manifest.json`. Refresh the browser after adding it. |
| **Images not displaying** | Check the relative path. The path is relative to `index.html`, not the JSON file. Example: `questions/images/fig1.png`. |
| **Math not rendering** | Check your `<latex>` tags are closed correctly. The CDN must be reachable for the first load of each session. |
| **Quiz Creator won't download** | Make sure you have at least one question saved in the list before clicking Download. |
| **Quiz shows 0 questions** | Open ⚙️ → Quiz Setup and make sure at least one tag is checked in each filter group. |

---

## 🏗️ Architecture (for developers)

The quiz player is a single `index.html` with no build step. All logic is vanilla JavaScript in an IIFE.

```
index.html
  ├── <style>      — All CSS (responsive + print styles)
  ├── <body>       — Screens: loading, start, quiz, result, review, settings modal
  └── <script>
        ├── state        — Quiz runtime state
        ├── profile      — Student profile (localStorage)
        ├── quizConfig   — Quiz settings (localStorage)
        ├── Filtering    — buildFilterOptions, applyFilters, updateFilteredCount
        ├── Timer        — startTick, stopTick, complexityLimit, autoSkipTimedOut
        ├── Quiz flow    — start, render, selectChoice, handleAnswer, advance, skip
        ├── Results      — showResults, showReview, backToResults
        ├── Print        — printQuiz
        └── window.App   — Public API bound to HTML onclick handlers
```

---


## 📄 Acknowledgements
The authors would like to thank Ms Sonam Patro for her support in reviewing all the questions related to Biology 
The authors would like to thank Mr Shivakumar K S for his support in reviewing all the questions related to Mathematics

## 📄 License

See [LICENSE](LICENSE).

