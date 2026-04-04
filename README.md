# 🟠 Inkspire — AI Content Generation Engine

Inkspire is an intelligent content generation system that uses a multi-agent AI pipeline to transform raw source material into polished **blog posts**, **social media threads**, and **email copy** — all fact-checked and verified.

---

## 🤖 How it Works

1. **Research Agent** — reads your raw input, extracts a verified Fact-Sheet (features, claims, audience, tone) and flags any ambiguous statements
2. **Copywriter Agent** — uses the Fact-Sheet as the single source of truth to generate a Blog, Social Thread, and Email
3. **Editor Agent** — reviews the content against the Fact-Sheet and approves or rejects it

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

## 🚀 Live Demo

- **Frontend:** [your-inkspire.vercel.app](https://your-inkspire.vercel.app)
- **Backend API:** [your-inkspire-backend.onrender.com](https://your-inkspire-backend.onrender.com)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| AI Model | Llama 3 via Groq API |
| Communication | REST API + UART |
| Deployment | Vercel (frontend), Render (backend) |

---

## 📋 API Endpoint

**POST** `/generate`

Request body:
```json
{
  "text": "Your raw content or brief here"
}
```

Response:
```json
{
  "fact_sheet": { ... },
  "content": "BLOG: ... THREAD: ... EMAIL: ...",
  "review": "APPROVED",
  "logs": [ "..." ],
  "flags": [ ... ]
}
```

---

## 👩‍💻 Authors

Built by Devika Vinod