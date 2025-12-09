from abc import ABC, abstractmethod

from domain.entities import CardFace


class ICardFaceRepository(ABC):
    @abstractmethod
    def create(self, card_face_data: CardFace) -> str:
        pass
