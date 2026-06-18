from pydantic import BaseModel
class ResumeTextRequest(BaseModel):
    text: str