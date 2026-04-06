# 🟠 Inkspire — AI Content Generation Engine

---

## The Problem

Creating consistent, fact-accurate marketing content across multiple formats — blog posts, social threads, and emails — is time-consuming and error-prone. Writers frequently introduce inaccuracies or invented claims when working from raw source material. Existing AI tools generate content without verifying facts first, leading to unreliable outputs.

---

## The Solution

Inkspire uses a three-agent AI pipeline to transform raw source material into polished, fact-checked content:

- **Research Agent** — reads your raw input and extracts a verified Fact-Sheet (product features, key claims, target audience, tone). Flags any ambiguous statements. This Fact-Sheet is the single source of truth for all content generation.
- **Copywriter Agent** — uses only the Fact-Sheet to generate a Blog Post, Social Thread, and Email. Cannot invent facts not present in the Fact-Sheet.
- **Editor Agent** — cross-checks the generated content against the Fact-Sheet and either approves it or rejects it with a reason, triggering a regeneration if needed.

The frontend displays the Fact-Sheet in real time so users can verify what the AI extracted before trusting the output. Each content format (Blog, Thread, Email) has independent Copy, Approve, and Regenerate controls.

---

## Tech Stack

| Category | Technology |
|----------|-----------|
| Programming Languages | Python, JavaScript |
| Backend Framework | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| AI Model | Llama 3.1 (via Groq API) |
| HTTP Client | Python `requests`, browser `fetch` |
| Environment Variables | `python-dotenv` |
| Dependencies | `openai`, `uvicorn`, `pydantic` |

---

## 🗂️ Project Structure
Content_factory/
├── main.py              # FastAPI backend — main entry point
├── .env                 # API keys (not committed to GitHub)
├── requirements.txt     # Python dependencies
├── agents/
│   ├── utils.py         # Groq LLM client (shared)
│   ├── research.py      # Research & Fact-Check Agent
│   ├── copywriter.py    # Copywriter Agent
│   └── editor.py        # Editor Agent
└── static/
├── index.html       # Frontend UI
├── script.js        # API calls and UI logic
└── style.css        # Styling


----------------------------------------------


## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Devikaa03/InkSpire.git
cd InkSpire
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder:

Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the backend
```bash
uvicorn main:app --reload
```
Backend will start at `http://127.0.0.1:8000`

### 5. Open the frontend
In a second terminal:
```bash
cd static
python -m http.server 5500
```
Then open `http://localhost:5500` in your browser.

---

## 👩‍💻 Authors

Built by Devika Vinod