from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class CardRulling(BaseEntity):
    card_id: str
    oracle_id: str
    source: str
    published_at: str
    comment: str
