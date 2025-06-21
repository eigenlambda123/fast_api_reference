from fastapi import FastAPI

app = FastAPI()


@app.get("/keyword-weights/", response_model=dict[str, float]) # Using a dictionary with string keys and float values as the response model
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}