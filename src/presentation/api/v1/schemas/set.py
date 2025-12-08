from typing import Generic, Optional, TypeVar
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

T = TypeVar("T")


class SetTypeResponseDTO(BaseModel):
    id: UUID = Field(..., description="The unique identifier of the set type")
    name: str = Field(..., description="The name of the set type")
    description: str = Field(..., description="The description of the set type")


class BaseSetDTO(BaseModel):
    name: str = Field(..., description="The name of the set")
    code: str = Field(..., description="The code of the set")
    card_count: int = Field(..., description="The number of cards in the set")
    release_date: str = Field(
        ..., description="The release date of the set in YYYY-MM-DD format"
    )
    is_digital: bool = Field(..., description="Indicates if the set is digital")
    is_foil_only: bool = Field(
        ..., description="Indicates if the set contains only foil cards"
    )
    is_non_foil_only: bool = Field(
        ..., description="Indicates if the set contains only non-foil cards"
    )
    icon_uri: str = Field(..., description="The URI for the set icon image")


class CreateSetDTO(BaseSetDTO):
    set_type_id: UUID = Field(..., description="The unique identifier of the set type")
    external_id: UUID = Field(..., description="The external identifier of the set")

    @field_validator("external_id", "set_type_id")
    def to_str(cls, v):
        return str(v)


class ListSetsQueryParamsDTO(BaseModel):
    limit: Optional[int] = Field(
        5, description="The maximum number of sets to return", ge=1, le=100
    )
    cursor: Optional[str] = Field(
        None, description="The cursor for pagination to fetch the next set of results"
    )
    order: Optional[str] = Field(
        default="asc", pattern="^(asc|desc)$", description="Ordering direction"
    )


class SetResponseDTO(BaseSetDTO):
    id: UUID = Field(..., description="The unique identifier of the set")
    set_type: SetTypeResponseDTO = Field(
        ..., description="The type information of the set"
    )


class CreateSetResponseDTO(BaseModel):
    id: UUID = Field(..., description="The unique identifier of the created set")


class PaginatedResponseDTO(BaseModel, Generic[T]):
    items: list[T] = Field(..., description="List of items in the current page")
    next_cursor: Optional[str] = Field(
        None,
        description="Cursor to fetch the next page, or None if this is the last page",
    )
