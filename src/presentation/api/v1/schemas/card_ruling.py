from pydantic import BaseModel, Field


class CreateCardRulingDTO(BaseModel):
    card_id: str = Field(
        description="The unique identifier (UUID) of the card this rulling belongs to."
    )
    source: str = Field(description="Source of the rulling.")
    published_at: str = Field(description="Publication date of the rulling.")
    comment: str = Field(description="The text of the rulling.")


class CardRulingResponseDTO(BaseModel):
    id: str = Field(description="The unique identifier (UUID) of the card ruling.")
