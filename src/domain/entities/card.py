from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class Card(BaseEntity):
    external_id: str
    set_id: str
    name: str
    lang: str
    layout: str
    rarity: str
    mana_cost: str
    cmc: int
    type_line: str
    oracle_text: str
    power: str
    toughness: str
    loyalty: str
