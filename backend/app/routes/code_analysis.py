from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from ..services.lm_service import LMStudioService

router = APIRouter()
lm_service = LMStudioService()

class CodeAnalysisRequest(BaseModel):
    code: str

class CodeRefactorRequest(BaseModel):
    code: str
    instructions: str

@router.post("/analyze")
async def analyze_code(request: CodeAnalysisRequest):
    """Analyze code using the LM Studio model."""
    try:
        result = await lm_service.analyze_code(request.code)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/refactor")
async def refactor_code(request: CodeRefactorRequest):
    """Refactor code based on instructions using the LM Studio model."""
    try:
        result = await lm_service.refactor_code(request.code, request.instructions)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))