from pydantic import BaseModel, Field


class PginationQueryParam(BaseModel):
    limit: int | None = Field(
        5, description="The maximum number of sets to return", ge=1, le=100
    )
    cursor: str | None = Field(
        None, description="The cursor for pagination to fetch the next set of results"
    )
    order: str | None = Field(
        default="asc", pattern="^(asc|desc)$", description="Ordering direction"
    )
