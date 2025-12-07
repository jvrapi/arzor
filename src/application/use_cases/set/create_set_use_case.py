from domain.entities import Set
from domain.exceptions import EntityAlreadyExistsError
from domain.ports.repositories import FindSetProps, ISetRepository

from .dto import CreateSetInput


class CreateSetUseCase:
    def __init__(self, set_repository: ISetRepository):
        self._set_repository = set_repository

    async def execute(self, input: CreateSetInput) -> str:
        """
        Cria um novo set com os dados fornecidos.

        Args:
            input (CreateSetInput): Dados necessários para criar o set.

        Returns:
            str: O ID do set criado.
        """

        set_already_exists = await self._set_repository.get_by(
            FindSetProps(code=input.code)
        )

        if set_already_exists:
            raise EntityAlreadyExistsError(
                f"Set with code '{input.code}' already exists."
            )

        set_entity = Set(**input.model_dump())
        created_set_id = await self._set_repository.create(set_entity)
        return created_set_id
