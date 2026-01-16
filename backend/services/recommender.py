def recommend_learning(missing_skills):
    recommendations = {}

    for skill in missing_skills:
        recommendations[skill] = {
            "course": f"Intro to {skill}",
            "platform": "Coursera / Udemy",
            "duration": "2–4 weeks"
        }

    return recommendations
