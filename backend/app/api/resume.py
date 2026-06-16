from fastapi import APIRouter, UploadFile, File
from io import BytesIO
from pypdf import PdfReader

router = APIRouter()

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