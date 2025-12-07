from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class FindSetProps:
    id: UUID | None = None
    code: str | None = None
    external_id: str | None = None
