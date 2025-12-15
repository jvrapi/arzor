from domain.entities import Card, CardFace
from domain.ports.repositories import ICardRepository

from .dto import CreateCardInput


class CreateCardUseCase:
    def __init__(self, card_repository: ICardRepository):
        self._card_repository = card_repository

    async def execute(self, inputs: list[CreateCardInput]) -> list[str]:
        cards = []

        for dto in inputs:
            faces = [
                CardFace(card_id=None, **face.model_dump()) for face in dto.faces or []
            ]

            card = Card(**dto.model_dump(exclude={"faces"}), faces=faces)

            cards.append(card)

        created_ids = await self._card_repository.create_many(cards)

        return created_ids
