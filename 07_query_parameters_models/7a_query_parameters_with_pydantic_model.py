from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    """
    A Pydantic model to define query parameters for filtering items.
    This model includes parameters for pagination, ordering, and filtering by tags.
    """
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at" 
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]): # use Annotated to include Pydantic model as query parameter
    return filter_query