from domain.entities import Card
from domain.ports.repositories import ICardRepository
from domain.value_objects import OrderType, PaginatedResult


class ListCardsUseCase:
    def __init__(self, card_repository: ICardRepository):
        self.card_repository = card_repository

    async def execute(
        self,
        limit: int | None = 5,
        cursor: str | None = None,
        order: OrderType | None = "asc",
        set_id: str | None = None,
        add_set_info: bool = False,
    ) -> PaginatedResult[Card]:
        return await self.card_repository.list(
            cursor=cursor,
            limit=limit,
            order=order,
            set_id=set_id,
            add_set_info=add_set_info,
        )
