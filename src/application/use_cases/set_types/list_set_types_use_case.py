from domain.ports.repositories import ISetTypeRepository
from src.domain.entities import SetType


class ListSetTypesUseCase:
    def __init__(self, set_type_repository: ISetTypeRepository):
        self._set_type_repository = set_type_repository

    async def execute(self) -> list[SetType]:
        return await self._set_type_repository.list()
