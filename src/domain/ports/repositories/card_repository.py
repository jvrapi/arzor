from abc import ABC, abstractmethod

from domain.entities import Card


class ICardRepository(ABC):
    @abstractmethod
    async def create_many(self, cards: list[Card]) -> str:
        pass
