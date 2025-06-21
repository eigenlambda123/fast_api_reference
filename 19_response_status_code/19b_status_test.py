from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED) # Use status from fastapi
async def create_item(name: str):
    return {"name": name}
