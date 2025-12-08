from abc import ABC, abstractmethod
from typing import Optional

from domain.entities import Set
from domain.value_objects import OrderType, PaginatedResult

from .set_query_params import FindSetProps


class ISetRepository(ABC):
    @abstractmethod
    async def list(
        self,
        limit: int = 5,
        cursor: Optional[str] = None,
        order: OrderType = "asc",
    ) -> PaginatedResult[Set]:
        pass

    @abstractmethod
    async def create(self, set_entity: Set) -> str:
        pass

    @abstractmethod
    async def get_by(self, find_props: FindSetProps) -> Set | None:
        pass
