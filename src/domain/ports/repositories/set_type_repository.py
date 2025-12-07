from abc import ABC, abstractmethod

from domain.entities import SetType


class ISetTypeRepository(ABC):
    @abstractmethod
    async def list(self) -> list[SetType]:
        pass
