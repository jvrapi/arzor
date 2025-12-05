from uuid import UUID

from pydantic import BaseModel, Field


class SetTypeResponseDTO(BaseModel):
    id: UUID = Field(..., description="The unique identifier of the set type")
    name: str = Field(..., description="The name of the set type")
    description: str = Field(..., description="The description of the set type")


class CreateSetDTO(BaseModel):
    name: str = Field(..., description="The name of the set")
    set_type_id: UUID = Field(..., description="The unique identifier of the set type")
    card_count: int = Field(..., description="The number of cards in the set")
    release_date: str = Field(
        ..., description="The release date of the set in YYYY-MM-DD format"
    )
    is_digital: bool = Field(..., description="Indicates if the set is digital")
    is_foil_only: bool = Field(
        ..., description="Indicates if the set contains only foil cards"
    )
    is_nonfoil_only: bool = Field(
        ..., description="Indicates if the set contains only non-foil cards"
    )


class CreateSetResponseDTO(BaseModel):
    id: UUID = Field(..., description="The unique identifier of the created set")
