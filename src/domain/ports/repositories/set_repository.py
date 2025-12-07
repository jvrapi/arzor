from abc import ABC, abstractmethod

from domain.entities import Set

from .set_query_params import FindSetProps


class ISetRepository(ABC):
    @abstractmethod
    async def list(self) -> list[Set]:
        pass

    @abstractmethod
    async def create(self, set_entity: Set) -> str:
        pass

    @abstractmethod
    async def get_by(self, find_props: FindSetProps) -> Set | None:
        pass
