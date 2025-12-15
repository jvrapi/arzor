from fastapi import APIRouter, Depends, status

from application.use_cases.set import CreateSetUseCase, ListSetsUseCase
from application.use_cases.set_types import ListSetTypesUseCase
from domain.ports.repositories import ISetRepository, ISetTypeRepository
from presentation.api.dependencies import get_set_repository, get_set_type_repository
from presentation.api.v1.schemas import (
    CreateSetDTO,
    CreateSetResponseDTO,
    PaginatedResponseDTO,
    SetResponseDTO,
    SetTypeResponseDTO,
)

router = APIRouter(tags=["set"], prefix="/sets")


@router.get("/types")
async def list_set_types(
    set_type_repository: ISetTypeRepository = Depends(get_set_type_repository),
) -> list[SetTypeResponseDTO]:
    """
    Lista todos os tipos de set disponíveis.
    """
    use_case = ListSetTypesUseCase(set_type_repository)
    result = await use_case.execute()

    return [
        SetTypeResponseDTO(
            id=set_type.id,
            name=set_type.name,
            description=set_type.description,
        )
        for set_type in result
    ]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_set(
    raw: CreateSetDTO, set_repository: ISetRepository = Depends(get_set_repository)
) -> CreateSetResponseDTO:
    """
    Cria um novo set com os dados fornecidos.
    """
    use_case = CreateSetUseCase(set_repository)
    result = await use_case.execute(raw)

    return CreateSetResponseDTO(id=result)


@router.get("/")
async def list_sets(
    set_repository: ISetRepository = Depends(get_set_repository),
) -> PaginatedResponseDTO[SetResponseDTO]:
    use_case = ListSetsUseCase(set_repository)
    result = await use_case.execute()
    return PaginatedResponseDTO[SetResponseDTO](
        items=[
            SetResponseDTO(
                id=set_.id,
                name=set_.name,
                code=set_.code,
                set_type_id=set_.set_type_id,
                card_count=set_.card_count,
                release_date=set_.release_date,
                is_digital=set_.is_digital,
                is_foil_only=set_.is_foil_only,
                is_nonfoil_only=set_.is_nonfoil_only,
                icon_uri=set_.icon_uri,
                set_type=SetTypeResponseDTO(
                    id=set_.set_type.id,
                    name=set_.set_type.name,
                    description=set_.set_type.description,
                ),
            )
            for set_ in result.items
        ],
        next_cursor=result.next_cursor,
    )
