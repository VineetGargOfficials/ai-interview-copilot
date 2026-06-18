from pydantic import BaseModel

class RoadmapRequest(BaseModel):
    missing_skills: list[str]