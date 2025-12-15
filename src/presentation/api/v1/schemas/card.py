from datetime import date

from pydantic import BaseModel, Field

from domain.value_objects import (
    BorderColor,
    Color,
    Finish,
    ImageUris,
    Legalities,
    Rarity,
    SecurityStamp,
)


class CreateCardResponseDTO(BaseModel):
    id: str = Field(description="A unique identifier (UUID) for the created card.")


class BaseCreateCardDTO(BaseModel):
    name: str = Field(description="The card’s name.")

    oracle_id: str | None = Field(
        default=None,
        description="Oracle ID from Scryfall — identifies the card's oracle identity (shared across different prints).",
    )

    mana_cost: str | None = Field(
        default=None,
        description="Mana cost of the card in MTG notation (e.g., '{3}{U}{W}'). May be null if not applicable.",
    )

    type_line: str | None = Field(
        default=None, description="Type line of the card (as per Scryfall Oracle data)."
    )

    oracle_text: str | None = Field(
        default=None, description="Oracle text (rules text) of the card."
    )

    power: str | None = Field(
        default=None,
        description="Power value (for creature cards). Null for non-creatures.",
    )

    toughness: str | None = Field(
        default=None,
        description="Toughness value (for creature cards). Null for non-creatures.",
    )

    loyalty: str | None = Field(
        default=None,
        description=(
            "The loyalty value printed on the card, used only for planeswalkers. "
            "It represents how much loyalty the planeswalker enters the battlefield with, "
            "or gains/loses through abilities. Null for non-planeswalker cards."
        ),
    )

    image_uris: ImageUris | None = Field(
        default=None,
        description="URLs for various image sizes/crops for this card. As provided by Scryfall.",
    )

    colors: list[Color] | None = Field(
        default=None, description="Colors of the card (e.g. ['U', 'W'])."
    )

    color_identity: list[Color] | None = Field(
        default=None,
        description="Color identity of the card (for deck-building restrictions).",
    )

    cmc: int | None = Field(
        default=0, description="Converted mana cost (mana value) of this card."
    )


class CreateCardFaceDTO(BaseCreateCardDTO):
    pass


class CreateCardDTO(BaseCreateCardDTO):
    set_id: str = Field(
        description="Scryfall set ID that identifies the set this card belongs to."
    )

    external_id: str = Field(description="External id of printed card")

    lang: str = Field(
        description="The language code of this card printing (e.g. 'en', 'pt', ...)."
    )

    released_at: date = Field(
        description="Release date of this card printing (YYYY-MM-DD)."
    )

    layout: str = Field(
        description="Layout type of this card (normal, split, transform, modal_dfc, etc.)."
    )

    keywords: list[str] | None = Field(
        default=None,
        description="List of keyword abilities (e.g. 'Flying', 'Companion', etc.).",
    )

    legalities: Legalities = Field(
        description="Legality of the card in all supported formats."
    )

    collector_number: str = Field(
        description="Collector number of this card within its set."
    )

    rarity: Rarity = Field(
        description="Rarity of the card (common, uncommon, rare, mythic, special, bonus)."
    )

    border_color: BorderColor = Field(
        description="Border color of the card as specified by Scryfall."
    )

    security_stamp: SecurityStamp | None = Field(
        default=None, description="Security stamp type (if any) for this card printing."
    )

    finishes: list[Finish] = Field(
        description="List of finishes available for this card (foil, nonfoil, etched, etc.)."
    )

    faces: list[CreateCardFaceDTO] | None = Field(
        default=None, description="Card faces, if any."
    )

    is_reserved: bool = Field(description="True if the card is on the Reserved List.")

    is_game_changer: bool = Field(
        description="True if the card is flagged as a 'game-changer' by Scryfall."
    )

    is_oversized: bool = Field(
        description="True if the card is oversized (e.g. oversized promo)."
    )

    is_promo: bool = Field(description="True if the card is a promotional printing.")

    is_reprint: bool = Field(description="True if the card is a reprint.")

    is_variation: bool = Field(
        description="True if this printing is a variant (alternate art / version)."
    )

    is_full_art: bool = Field(description="True if this is a full-art card version.")

    is_textless: bool = Field(
        description="True if this card has no rules text (textless variant)."
    )

    is_found_on_booster: bool = Field(
        description="True if this card can appear in boosters (booster-legal)."
    )
