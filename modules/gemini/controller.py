import base64
import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from modules.gemini.service import GeminiService
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(
    tags=["Gemini"],
)

@router.post("/extract-info")
async def extract_infor(file: UploadFile = File(...), gemini_service: GeminiService = Depends()):
    MAX_FILE_SIZE = int(os.getenv('MAX_SIZE')) * 1024 * 1024
    file_bytes = await file.read()
    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB limit")
    try:
        base64_str = base64.b64encode(file_bytes).decode("utf-8")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to encode image")
    return gemini_service.extract_text(base64_str)
