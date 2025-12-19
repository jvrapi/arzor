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


class ListSetsDTO(BaseModel):
    limit: int = 20
    cursor: str | None = None
    order: OrderType = "asc"


class FindSetProps(BaseModel):
    id: str | None = None
    external_id: str | None = None
    code: str | None = None
