from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/pdf", tags=["pdf"])

PDF_FOLDER = "./app/asset"

@router.get("/")
async def list_pdfs():
    """ Trả về danh sách file PDF có trong thư mục """
    files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    return {"files": files}

@router.get("/{filename}")
async def get_pdf(filename: str):
    """ Trả về file PDF theo tên """
    file_path = os.path.join(PDF_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf")
    return {"error": "File not found"}
