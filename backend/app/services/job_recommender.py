from app.services.skill_extractor import skill_extractor

JOB_ROLE_SKILLS = {
    "AI Engineer": [
        "Python",
        "Machine Learning",
        "LangChain",
        "Docker"
    ],
    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "Git"
    ],
    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],
    "ML Engineer": [
        "Python",
        "TensorFlow",
        "Docker",
        "Git"
    ]
}

def candidate_skills(skills: list[str])-> dict:
    recommendations = []

    skill_set = set(skills)

    for role, required_skills in JOB_ROLE_SKILLS.items():
        matched_skills = [
            skill
            for skill in required_skills
            if skill in skill_set
        ]

        match_score = len(matched_skills) / len(required_skills)

        recommendations.append({
            "role": role,
            "match_score": round(match_score * 100, 2) ,
            "matched_skills": matched_skills,
            "missing_skills" : [
                skill 
                for skill in required_skills
                if skill not in skill_set 
            ]
        })

    recommendations.sort(
        key = lambda x: x["match_score"],
        reverse = True
    )

    return{
        "recommendations": recommendations
    }

