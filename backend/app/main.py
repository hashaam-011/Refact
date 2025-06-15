from fastapi import FastAPI
from app.routes import analyze

app = FastAPI(title="RefactAI Backend")

app.include_router(analyze.router, prefix="/api/analyze", tags=["Analyze"])

@app.get("/")
def root():
    return {"message": "RefactAI backend is running"}
