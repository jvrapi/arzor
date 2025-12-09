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


class CreateCardInput(BaseModel):
    external_id: str
    set_id: str
    oracle_id: str
    name: str
    lang: str
    released_at: date
    layout: str

    image_uris: ImageUris

    cmc: int
    type_line: str
    oracle_text: str

    mana_cost: str | None
    power: str | None
    toughness: str | None
    loyalty: str | None

    colors: list[Color]
    color_identity: list[Color]
    keywords: list[str]

    legalities: Legalities

    collector_number: str
    rarity: Rarity
    border_color: BorderColor
    security_stamp: SecurityStamp | None

    finishes: list[Finish]

    is_reserved: bool
    is_game_changer: bool
    is_foil: bool
    is_non_foil: bool
    is_oversized: bool
    is_promo: bool
    is_reprint: bool
    is_variation: bool
    is_full_art: bool
    is_textless: bool
    is_found_on_booster: bool
