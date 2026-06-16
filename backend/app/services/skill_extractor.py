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

    return {
        "skills": sorted(list(detected_skills))
    }

