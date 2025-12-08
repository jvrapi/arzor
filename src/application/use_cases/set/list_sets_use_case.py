from typing import Optional

from domain.entities import Set
from domain.ports.repositories import ISetRepository
from domain.value_objects import OrderType, PaginatedResult


class ListSetsUseCase:
    def __init__(self, set_repository: ISetRepository):
        self._set_repository = set_repository

    async def execute(
        self,
        limit: int = 5,
        cursor: Optional[str] = None,
        order: OrderType = "asc",
    ) -> PaginatedResult[Set]:
        return await self._set_repository.list(
            limit=limit,
            cursor=cursor,
            order=order,
        )
