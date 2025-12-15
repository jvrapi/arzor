from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel

from domain.value_objects import OrderType


class CreateSetInput(BaseModel):
    name: str
    external_id: str
    code: str
    set_type_id: str
    card_count: int
    release_date: str
    is_digital: bool
    is_foil_only: bool
    is_nonfoil_only: bool
    icon_uri: str


@dataclass
class ListSetsDTO:
    limit: int = 20
    cursor: Optional[str] = None
    order: OrderType = "asc"
