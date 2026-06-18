from app.utils.api_response import (success_response, failure_response)
JOB_ROLE_SKILLS = {
    "AI Engineer": {
        "Python",
        "Machine Learning",
        "LangChain",
        "Docker"
    },
    "Backend Developer": {
        "Python",
        "FastAPI",
        "SQL",
        "Git"
    },
    "Data Scientist": {
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning"
    },
    "ML Engineer": {
        "Python",
        "TensorFlow",
        "Docker",
        "Git"
    }
}

def target_role(role: str, skills: list[str])-> dict:
    target = []
    skill_set = set(skills)
    for my_role,required_skills in JOB_ROLE_SKILLS.items():
        if my_role.lower() == role.lower():
            matched_skill = [
                skill
                for skill in required_skills
                if skill in skill_set
            ]

            missing_skill =  [
                    skill
                    for skill in required_skills
                    if skill not in skill_set
                ]

            return success_response({
                "role": role,
                "existing_skill": matched_skill,
                "missing_skills": missing_skill,
            })
            
        
    return {
        "error": f"Role '{role}' not found"
    }

    



