from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    """Dependency to extract query parameter 'q'"""
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    """Dependency that uses another dependency to extract 'q' and checks for a cookie"""
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    """Endpoint that uses sub-dependency to get 'q' or cookie value"""
    return {"q_or_cookie": query_or_default}