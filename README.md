# AI Research Assistant

A FastAPI-based AI research tool that generates summaries on any topic using Groq's Llama AI model.

## Features
- FastAPI REST API
- Groq AI integration (Llama 3.3 70B model)
- Research topic summarization
- Error handling
- Pydantic data validation

## Tech Stack
- **Backend:** FastAPI
- **AI Model:** Groq (Llama 3.3 70B)
- **Language:** Python
- **Deployment:** Render (upcoming)

## Installation

1. Clone the repository
```bash
git clone https://github.com/shivam-logic/AI-Research-Assistant.git
cd AI-Research-Assistant
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file
```bash
GROQ_API_KEY=your_groq_api_key_here
```

5. Run the server
```bash
uvicorn main:app --reload
```

## API Usage

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### POST /research
Request:
```json
{
  "topic": "Python 3.12 new features"
}
```

Response:
```json
{
  "topic": "Python 3.12 new features",
  "summary": "AI generated summary here..."
}
```

## Next Features
- YouTube video summarization
- RAG with PDF upload
- Multi-topic research
- Response caching

## Author
Shivam Chaurasia

## License
MIT
