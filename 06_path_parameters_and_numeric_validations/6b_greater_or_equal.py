from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
): # use ge (greater than or equal) validation on path parameter item_id
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results