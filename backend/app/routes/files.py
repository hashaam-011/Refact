from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import File
from pydantic import BaseModel

router = APIRouter()

class FileCreate(BaseModel):
    filename: str
    content: str

class FileResponse(BaseModel):
    id: int
    filename: str
    content: str

    class Config:
        from_attributes = True

@router.post("/", response_model=FileResponse)
def create_file(file: FileCreate, db: Session = Depends(get_db)):
    db_file = File(filename=file.filename, content=file.content)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

@router.get("/", response_model=List[FileResponse])
def get_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    files = db.query(File).offset(skip).limit(limit).all()
    return files

@router.get("/{file_id}", response_model=FileResponse)
def get_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(File).filter(File.id == file_id).first()
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file