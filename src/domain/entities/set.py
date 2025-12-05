from dataclasses import dataclass

from .base import BaseEntity


@dataclass(frozen=True)
class Set(BaseEntity):
    set_type_id: str
    external_id: str
    code: str
    name: str
    card_count: int
    release_date: str
    is_digital: bool
    is_foil_only: bool
    is_nonfoil_only: bool
