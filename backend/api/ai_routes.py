from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.gemini_service import query_gemini

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str

@router.post("/ask")
async def ask_ai(req: AIRequest):
    return {"response": query_gemini(req.prompt)}
