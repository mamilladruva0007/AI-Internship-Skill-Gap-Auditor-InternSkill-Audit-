import json

with open("backend/data/internship_roles.json") as f:
    ROLES = json.load(f)

def analyze_skill_gap(candidate_skills, role):
    required_skills = ROLES.get(role, [])
    matched = [s for s in candidate_skills if s in required_skills]
    missing = [s for s in required_skills if s not in candidate_skills]

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }
