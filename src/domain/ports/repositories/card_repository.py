from abc import ABC, abstractmethod

from domain.entities import Card
from domain.value_objects import OrderType, PaginatedResult


class ICardRepository(ABC):
    @abstractmethod
    async def create_many(self, cards: list[Card]) -> str:
        pass

    @abstractmethod
    async def list(
        self,
        limit: int | None = 5,
        cursor: str | None = None,
        order: OrderType | None = "asc",
        set_id: str | None = None,
        add_set_info: bool = False,
    ) -> PaginatedResult[Card]:
        pass
