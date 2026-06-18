from app.utils.api_response import (success_response, failure_response)
SKILL_KEYWORD = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "TensorFlow",
    "PyTorch",
    "FastAPI",
    "Docker",
    "Git",
    "Machine Learning",
    "Deep Learning",
    "LangChain",
    "LangGraph",
    "Pandas",
    "NumPy"
]

def skill_extractor(text: str) -> dict:
    text = text.lower()

    detected_skills = set()

    for skill in SKILL_KEYWORD:
        if skill.lower() in text:
            detected_skills.add(skill)

    return success_response({
        "skills": sorted(list(detected_skills))
    })

