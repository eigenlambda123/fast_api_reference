from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)], #  use gt (greater than) and le (less than or equal) validations on path parameter item_id
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results