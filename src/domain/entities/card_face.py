from dataclasses import dataclass

from domain.value_objects import (
    Color,
    ImageUris,
)

from .base import BaseEntity


@dataclass(frozen=True)
class CardFace(BaseEntity):
    card_id: str | None
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
