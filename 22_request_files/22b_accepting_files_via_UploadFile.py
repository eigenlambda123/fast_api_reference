from typing import Annotated

from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile): # Use UploadFile to handle file uploads
    return {"filename": file.filename}