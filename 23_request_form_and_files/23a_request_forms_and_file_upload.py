from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()], # file as bytes
    fileb: Annotated[UploadFile, File()], # file as UploadFile
    token: Annotated[str, Form()] # token as a form field
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }