from dataclasses import dataclass

from domain.value_objects import (
    BorderColor,
    Color,
    Finish,
    ImageUris,
    Legalities,
    Rarity,
    SecurityStamp,
)

from .base import BaseEntity
from .card_face import CardFace
from .set import Set


@dataclass(frozen=True)
class Card(BaseEntity):
    external_id: str
    set_id: str
    oracle_id: str
    name: str
    lang: str
    released_at: str
    layout: str
    image_uris: ImageUris
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
    mana_cost: str | None
    cmc: int | None
    type_line: str
    oracle_text: str | None
    power: str | None
    toughness: str | None
    loyalty: str | None
    colors: list[Color] | None
    color_identity: list[Color] | None
    keywords: list[str] | None
    legalities: Legalities
    faces: list[CardFace] | None
    set: Set | None = None
