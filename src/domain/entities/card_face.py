from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class CardFace(BaseEntity):
    card_id: str
    name: str
    mana_cost: str
    type_line: str
    oracle_text: str
    power: str
    toughness: str
    loyalty: str
