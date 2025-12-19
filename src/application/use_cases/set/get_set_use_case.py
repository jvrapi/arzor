from domain.entities import Set
from domain.exceptions import EntityNotFoundError, ValidationError
from domain.ports.repositories import FindSetProps, ISetRepository


class GetSetUseCase:
    def __init__(self, set_repository: ISetRepository):
        self._set_repository = set_repository

    async def execute(
        self,
        id: str | None = None,
        code: str | None = None,
        external_id: str | None = None,
        add_set_type_info: bool = False,
    ) -> Set:
        if not id and not code and not external_id:
            raise ValidationError("At least one identifier must be provided.")

        set_entity = None

        if id:
            set_entity = await self._set_repository.get_by(
                FindSetProps(id=id), add_set_type_info=add_set_type_info
            )
        elif code:
            set_entity = await self._set_repository.get_by(
                FindSetProps(code=code), add_set_type_info=add_set_type_info
            )
        else:
            set_entity = await self._set_repository.get_by(
                FindSetProps(external_id=external_id),
                add_set_type_info=add_set_type_info,
            )

        if not set_entity:
            raise EntityNotFoundError("Set not found.")

        return set_entity
