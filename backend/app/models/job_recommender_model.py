from pydantic import BaseModel
class SkillsRequest(BaseModel):
    skills: list[str]