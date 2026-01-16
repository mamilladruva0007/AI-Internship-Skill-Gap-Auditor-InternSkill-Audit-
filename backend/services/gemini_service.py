import os
import requests

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.0-flash:generateContent"
)

def query_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key not configured."

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": api_key
    }

    try:
        r = requests.post(GEMINI_URL, json=payload, headers=headers, timeout=15)

        if r.status_code == 429:
            return (
                "Gemini quota exhausted. "
                "This is a fallback response demonstrating integration."
            )

        if r.status_code != 200:
            return "Gemini service error."

        data = r.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception:
        return "Gemini service unavailable."
