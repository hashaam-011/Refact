from fastapi import APIRouter, UploadFile, File
import os
import uuid
from app.config import settings
from app.services.file_utils import save_uploaded_zip

router = APIRouter()

@router.post("/upload")
async def upload_repo(file: UploadFile = File(...)):
    repo_id = str(uuid.uuid4())
    repo_path = os.path.join(settings.WORKSPACE_DIR, repo_id)
    os.makedirs(repo_path, exist_ok=True)

    await save_uploaded_zip(file, repo_path)

    return {"message": "File uploaded", "repo_id": repo_id}
