from dataclasses import dataclass

from .base import BaseEntity
from .set_type import SetType


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
    is_non_foil_only: bool
    icon_uri: str
    set_type: SetType | None = None
