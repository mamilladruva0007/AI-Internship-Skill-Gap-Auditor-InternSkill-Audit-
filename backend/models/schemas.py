from pydantic import BaseModel
from typing import List, Dict

class ResumeAnalysisResponse(BaseModel):
    extracted_skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    recommendations: Dict
