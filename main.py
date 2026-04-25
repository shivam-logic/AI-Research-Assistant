import os
from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi

# Load API key from .env file
load_dotenv()

# Connect to Groq using our API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Pydantic models - defines what user will send
class ResearchRequest(BaseModel):
    topic: str

class YouTubeRequest(BaseModel):
    url: str

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to AI Research Assistant", "status": "running"}

# Research route - takes topic and returns AI summary
@app.post("/research")
def research(request: ResearchRequest):
    try:
        # This is the prompt we send to Groq
        prompt = f"Research the following topic and give me a clear Summary: {request.topic}"

        # Call Groq and get response
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        # Return the result
        return {"topic": request.topic, "summary": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}

# YouTube summarizer route - takes URL and returns video summary
@app.post("/youtube-summary")
def youtube_summary(request: YouTubeRequest):
    try:
        # Extract video ID from URL
        if "v=" in request.url:
            video_id = request.url.split("v=")[1].split("&")[0]
        else:
            return {"error": "Invalid YouTube URL"}

        # Get transcript from YouTube
        fetcher = YouTubeTranscriptApi()
        transcript = fetcher.fetch(video_id)

        # Convert transcript to plain text
        full_text = " ".join([entry.text for entry in transcript])

        # Send to Groq for summary
        prompt = f"Summarize this YouTube video transcript clearly and concisely with key points:\n\n{full_text[:4000]}"

        # Call Groq and get response
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        # Return the result
        return {
            "url": request.url,
            "summary": response.choices[0].message.content
        }

    except Exception as e:
        return {"error": str(e)}