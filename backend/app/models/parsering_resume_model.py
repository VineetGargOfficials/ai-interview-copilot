from pydantic import BaseModel

class ParseringRequest(BaseModel):
    resume: str
