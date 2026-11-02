import os
from fastapi import FastAPI

app = FastAPI(title="Cloud Containers Lab", version="1.0")

@app.get("/")
def index():
    return {"message": "FastAPI in Docker", "version": "v1"}

@app.get("/health")
def health():
    return {"status": "ok", "version": "v1"}

@app.get("/info")
def info():
    return {
        "environment": os.getenv("APP_ENV", "local"),
        "student_group": os.getenv("STUDENT_GROUP", "not-set")
    }