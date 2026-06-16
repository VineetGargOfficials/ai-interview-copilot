from fastapi import APIRouter, UploadFile, File
from io import BytesIO
from pypdf import PdfReader
from pydantic import BaseModel

from app.services.skill_extractor import skill_extractor
from app.services.job_recommender import candidate_skills

router = APIRouter()

class ResumeTextRequest(BaseModel):
    text: str

class SkillsRequest(BaseModel):
    skills: list[str]

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    reader = PdfReader(BytesIO(pdf_bytes))

    full_text = ""

    for page in reader.pages:
        text = page.extract_text() or ""
        full_text += text + "\n"


    return{
        "page": len(reader.pages),
        "content_type": full_text[:100].strip(),
    }

@router.post("/extract-skills")
def extract_skills(request: ResumeTextRequest):
    return skill_extractor(request.text)

@router.post("/job-recommender")
def recommend_jobs(request: SkillsRequest):
    return candidate_skills(request.skills)