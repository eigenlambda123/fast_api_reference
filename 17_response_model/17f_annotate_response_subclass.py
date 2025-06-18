from fastapi.responses import RedirectResponse

@app.get("/teleport")
async def get_teleport() -> RedirectResponse:  # Specific subclass annotation
    return RedirectResponse(url="https://youtu.be/dQw4w9WgXcQ")  # 302 Redirect