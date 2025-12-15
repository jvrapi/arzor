from abc import ABC, abstractmethod

from domain.entities import CardFace


class ICardFaceRepository(ABC):
    @abstractmethod
    def create_many(self, card_faces: list[CardFace]) -> list[str]:
        pass
