from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message: " "AI interview copilot is running"}

app.include_router(resume_router)