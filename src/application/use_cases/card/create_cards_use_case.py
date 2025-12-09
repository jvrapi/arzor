from domain.entities import Card
from domain.ports.repositories import ICardRepository

from .dto import CreateCardInput


class CreateCardUseCase:
    def __init__(self, card_repository: ICardRepository):
        self._card_repository = card_repository

    async def execute(self, inputs: list[CreateCardInput]) -> list[str]:
        created_ids = await self._card_repository.create_many(
            cards=[Card(**c.model_dump()) for c in inputs]
        )

        return created_ids
