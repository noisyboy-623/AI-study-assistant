# app/routes/summarize.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from app.features.summarization.services.summarizer_factory import get_summarizer

load_dotenv()

router = APIRouter()

# Define request body
class SummaryRequest(BaseModel):
    text: str

# Cohere Summarization Function
def cohere_summarize(text: str) -> str:
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Cohere API key not found in environment variables.")

    url = "https://api.cohere.ai/v1/summarize"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "length": "medium",         # short, medium, long
        "format": "bullets",      # paragraph, bullets
        "model": "command"          # the summarization model
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json().get("summary", "No summary returned.")

# FastAPI route
@router.post("/summarize")
def summarize_text(request: SummaryRequest):
    try:
        summary = cohere_summarize(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
