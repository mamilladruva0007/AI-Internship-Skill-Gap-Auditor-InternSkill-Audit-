import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer

with open("backend/data/skill_taxonomy.json") as f:
    SKILLS = json.load(f)

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if re.search(rf"\b{skill.lower()}\b", text):
            found.append(skill)

    return list(set(found))
