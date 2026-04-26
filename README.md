# 🤖 AI Research Assistant

> A production-ready AI-powered research tool built with FastAPI and Groq LLM

[![FastAPI](https://img.shields.io/badge/FastAPI-0.135-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=flat)](https://groq.com)
[![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=flat&logo=render)](https://ai-research-assistant-imd2.onrender.com)

---

## 🚀 Live Demo

**Base URL:** [https://ai-research-assistant-imd2.onrender.com](https://ai-research-assistant-imd2.onrender.com)

**Interactive Docs:** [https://ai-research-assistant-imd2.onrender.com/docs](https://ai-research-assistant-imd2.onrender.com/docs)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Topic Research** | Enter any topic and get a detailed AI-generated summary |
| 🎥 **YouTube Summarizer** | Paste any YouTube URL and get key points extracted |
| 📄 **PDF Q&A (RAG)** | Upload any PDF and ask questions — AI answers from the document |
| ✅ **Data Validation** | Pydantic models ensure clean input handling |
| 🛡️ **Error Handling** | Graceful error responses instead of crashes |
| 📚 **Auto Documentation** | Swagger UI generated automatically by FastAPI |

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **AI Model:** Groq API (LLaMA 3.3 70B)
- **Language:** Python 3.14
- **Data Validation:** Pydantic
- **PDF Processing:** PyPDF2
- **Deployment:** Render
- **Version Control:** GitHub

---

## 📡 API Endpoints

### GET /
Health check — returns app status

### POST /research
Takes any research topic and returns an AI-generated summary.

**Request:**
```json
{
  "topic": "Python 3.12 new features"
}
```

**Response:**
```json
{
  "topic": "Python 3.12 new features",
  "summary": "Detailed AI summary here..."
}
```

### POST /youtube-summary
Takes a YouTube URL and returns a structured summary of the video content.

**Request:**
```json
{
  "url": "https://www.youtube.com/watch?v=your_video_id"
}
```

**Response:**
```json
{
  "url": "https://www.youtube.com/watch?v=your_video_id",
  "summary": "Key points from the video..."
}
```

### POST /pdf-qa
Upload any PDF file and ask a question. AI answers based only on the document content.

**Form Data:**
- `file` — PDF file to upload
- `question` — Your question about the document

**Response:**
```json
{
  "question": "What is this document about?",
  "answer": "AI-generated answer based on the PDF...",
  "pages_processed": 3
}
```

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/shivam-logic/AI-Research-Assistant.git
cd AI-Research-Assistant
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file**
GROQ_API_KEY=your_groq_api_key_here

**5. Run the server**
```bash
uvicorn main:app --reload
```

**6. Open docs**
http://127.0.0.1:8000/docs

---

## 🗂️ Project Structure
AI-Research-Assistant/
├── main.py              # FastAPI application
├── requirements.txt     # Project dependencies
├── .env                 # API keys (not pushed to GitHub)
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
---

## 🏗️ Architecture
User Request
↓
FastAPI (receives request)
↓
Pydantic (validates data)
↓
Groq API — LLaMA 3.3 70B (processes with AI)
↓
JSON Response (returned to user)
---

## 🔮 Upcoming Features

- [ ] Vector database integration for large document search
- [ ] Multi-document RAG support
- [ ] Conversation memory
- [ ] Authentication and rate limiting
- [ ] LangGraph agentic workflow

---

## 👨‍💻 Author

**Shivam Chaurasia**
- GitHub: [@shivam-logic](https://github.com/shivam-logic)
- LinkedIn: [shivam-chaurasia](https://linkedin.com/in/shivam-chaurasia-346a83145)

---

## 📄 License

MIT License — feel free to use and modify.
