from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.resume_parser import parse_resume
from backend.services.skill_extractor import extract_skills
from backend.services.skill_matcher import analyze_skill_gap
from backend.services.recommender import recommend_learning

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    role: str = "data_science"
):
    try:
        if not file.filename.lower().endswith((".pdf", ".docx")):
            raise HTTPException(status_code=400, detail="Invalid file format")

        resume_text = parse_resume(file)
        skills = extract_skills(resume_text)
        analysis = analyze_skill_gap(skills, role)
        recommendations = recommend_learning(analysis["missing_skills"])

        return {
            "extracted_skills": skills,
            "matched_skills": analysis["matched_skills"],
            "missing_skills": analysis["missing_skills"],
            "recommendations": recommendations
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
