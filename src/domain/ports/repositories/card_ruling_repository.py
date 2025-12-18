from abc import ABC, abstractmethod

from domain.entities import CardRuling


class ICardRulingRepository(ABC):
    @abstractmethod
    def create_many(self, card_rulings: list[CardRuling]) -> list[str]:
        pass
