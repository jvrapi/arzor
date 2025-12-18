from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class CardRuling(BaseEntity):
    card_id: str
    source: str
    published_at: str
    comment: str
