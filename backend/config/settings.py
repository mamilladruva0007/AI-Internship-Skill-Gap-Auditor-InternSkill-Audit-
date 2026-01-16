import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

# Read from os.environ ONLY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
