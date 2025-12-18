from pydantic import BaseModel, Field

from domain.value_objects import OrderType


class PaginationQueryParam(BaseModel):
    limit: int | None = Field(
        5, description="The maximum number of sets to return", ge=1, le=100
    )
    cursor: str | None = Field(
        None, description="The cursor for pagination to fetch the next set of results"
    )
    order: OrderType | None = Field(default="asc", description="Ordering direction")
