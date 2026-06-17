SKILL_ROADMAP = {
    "Python": {
        "priority": 1,
        "topics": [
            "Variables",
            "Functions",
            "OOP",
            "File Handling"
        ]
    },
    "Machine Learning": {
        "priority": 2,
        "topics": [
            "Linear Regression",
            "Classification",
            "Model Evaluation"
        ]
    },
    "LangChain": {
        "priority": 3,
        "topics": [
            "Chains",
            "Prompt Templates",
            "Retrievers",
            "Agents"
        ]
    }
}

def find_roadmap(skills: list[str])->dict:
    roadmap = []
    for skill in skills:
        for roadmap_skill, details in SKILL_ROADMAP.items():
            if roadmap_skill.lower() == skill.lower():
                roadmap.append({
                    "skill": skill,
                    "priority": details["priority"],
                    "topics": details["topics"]
                })   
        


    return {
        "roadmap": roadmap
    }