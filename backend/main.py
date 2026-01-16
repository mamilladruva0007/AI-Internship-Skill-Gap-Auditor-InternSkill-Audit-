from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings  # forces .env load

from backend.api.resume_routes import router as resume_router
from backend.api.ai_routes import router as ai_router

app = FastAPI(
    title="InternSkill Audit API",
    description="AI-powered Internship Skill Gap Auditor",
    version="1.0.0"
)

# --------------------
# CORS Configuration
# --------------------
# NOTE:
# allow_origins=["*"] is OK for development.
# In production, replace with your frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# API Routers
# --------------------
app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume Analysis"]
)

app.include_router(
    ai_router,
    prefix="/api/ai",
    tags=["AI Assistant"]
)

# --------------------
# Root Health Check
# --------------------
@app.get("/")
def root():
    return {"status": "InternSkill Audit API running"}
