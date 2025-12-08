from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class PaginatedResult(Generic[T]):
    items: list[T]
    next_cursor: Optional[str]
