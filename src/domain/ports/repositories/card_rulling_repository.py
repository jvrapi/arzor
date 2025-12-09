from abc import ABC, abstractmethod

from domain.entities import CardRulling


class ICardRullingRepository(ABC):
    @abstractmethod
    def create(self, card_rulling: CardRulling) -> str:
        pass
