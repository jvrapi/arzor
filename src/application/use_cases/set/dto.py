from pydantic import BaseModel


class CreateSetInput(BaseModel):
    name: str
    external_id: str
    code: str
    set_type_id: str
    card_count: int
    release_date: str
    is_digital: bool
    is_foil_only: bool
    is_non_foil_only: bool
