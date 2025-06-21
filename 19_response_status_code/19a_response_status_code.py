from fastapi import FastAPI

app = FastAPI()

@app.post("/items/", status_code=201) # Set status code to 201 Created
async def create_item(name: str):
    return {"name": name}