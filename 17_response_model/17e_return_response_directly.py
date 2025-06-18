from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:  # Base class annotation
    if teleport:
        return RedirectResponse(url="https://youtu.be/dQw4w9WgXcQ")  # 302 Redirect
    return JSONResponse(content={"message": "Portal ready"})  # Custom JSON