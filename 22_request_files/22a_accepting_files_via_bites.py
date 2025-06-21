from fastapi import FastAPI, File
from typing import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]): # Use File() to declare file upload as bytes
    return {"file_size": len(file)}

