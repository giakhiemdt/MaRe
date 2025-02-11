from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import pdf

app = FastAPI(title="FastAPI PDF Viewer")

# app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pdf.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI PDF Viewer!"}
