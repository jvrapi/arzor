from datetime import date

from pydantic import BaseModel

from domain.value_objects import (
    BorderColor,
    Color,
    Finish,
    ImageUris,
    Legalities,
    Rarity,
    SecurityStamp,
)


class BaseCreateCardInput(BaseModel):
    name: str
    oracle_id: str | None
    mana_cost: str | None
    type_line: str | None
    oracle_text: str | None
    power: str | None
    toughness: str | None
    loyalty: str | None
    image_uris: ImageUris | None
    colors: list[Color] | None
    color_identity: list[Color] | None
    oracle_text: str | None
    oracle_id: str | None
    image_uris: ImageUris | None
    cmc: int | None
    type_line: str | None


class CreateCardFaceInput(BaseCreateCardInput):
    pass


class CreateCardInput(BaseCreateCardInput):
    external_id: str
    set_id: str
    lang: str
    faces: list[CreateCardFaceInput]
    released_at: date
    layout: str

    keywords: list[str]

    legalities: Legalities

    collector_number: str
    rarity: Rarity
    border_color: BorderColor
    security_stamp: SecurityStamp | None

    finishes: list[Finish]

    is_reserved: bool
    is_game_changer: bool
    is_oversized: bool
    is_promo: bool
    is_reprint: bool
    is_variation: bool
    is_full_art: bool
    is_textless: bool
    is_found_on_booster: bool
