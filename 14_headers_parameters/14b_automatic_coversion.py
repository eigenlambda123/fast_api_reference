from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None, # Read a header without automatic conversion of underscores to dashes
    # The convert_underscores=False parameter prevents FastAPI from automatically converting underscores to dashes in the header name
):
    return {"strange_header": strange_header}