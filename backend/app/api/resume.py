from fastapi import APIRouter, UploadFile, File
from io import BytesIO
from pypdf import PdfReader

from app.services.skill_extractor import skill_extractor
from app.services.job_recommender import candidate_skills
from app.services.skill_gap_detector import target_role
from app.services.roadmap_generator import find_roadmap
from app.services.parsering_resume import parser

from app.models.skill_extractor_model import ResumeTextRequest
from app.models.skill_gap_detector_model import SkillGapRequest
from app.models.job_recommender_model import SkillsRequest
from app.models.roadmap_generator_model import RoadmapRequest
from app.models.parsering_resume_model import ParseringRequest

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    reader = PdfReader(BytesIO(pdf_bytes))

    full_text = ""

    for page in reader.pages:
        text = page.extract_text() or ""
        full_text += text + "\n"

    parsed_resume = parser(full_text)

    return{
        "page": len(reader.pages),
        "content_type": full_text[:100].strip(),
        "parsed_Resume": parsed_resume["data"]
    }

@router.post("/extract-skills")
def extract_skills(request: ResumeTextRequest):
    return skill_extractor(request.text)

@router.post("/job-recommender")
def recommend_jobs(request: SkillsRequest):
    return candidate_skills(request.skills)

@router.post("/skill-gap")
def find_skill_sap(request: SkillGapRequest):
    return target_role(request.role ,request.skills)

@router.post("/roadmap")
def create_roadmap(request: RoadmapRequest):
    return find_roadmap(request.missing_skills)

@router.post("/parser-resume")
def parseringResume(request: ParseringRequest):
    return parser(request.resume)