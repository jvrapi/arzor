from fastapi import APIRouter, Depends, status

from application.use_cases.set import CreateSetUseCase, GetSetUseCase, ListSetsUseCase
from application.use_cases.set_types import ListSetTypesUseCase
from domain.ports.repositories import ISetRepository, ISetTypeRepository
from presentation.api.dependencies import get_set_repository, get_set_type_repository
from presentation.api.v1.mappers import SetMapper
from presentation.api.v1.schemas import (
    BadRequestResponse,
    CreateSetDTO,
    CreateSetResponseDTO,
    GetSetParams,
    NotFoundResponse,
    PaginatedResponseDTO,
    PaginationQueryParam,
    SetResponseDTO,
    SetTypeResponseDTO,
)

router = APIRouter(tags=["Set"], prefix="/sets")


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


@router.post(
    "/", status_code=status.HTTP_201_CREATED, responses={400: BadRequestResponse}
)
async def create_set(
    raw: CreateSetDTO, set_repository: ISetRepository = Depends(get_set_repository)
) -> CreateSetResponseDTO:
    """
    Cria um novo set com os dados fornecidos.
    """
    use_case = CreateSetUseCase(set_repository)
    result = await use_case.execute(SetMapper.dto_to_input(raw))

    return CreateSetResponseDTO(id=result)


@router.get("/")
async def list_sets(
    set_repository: ISetRepository = Depends(get_set_repository),
    params: PaginationQueryParam = Depends(),
) -> PaginatedResponseDTO[SetResponseDTO]:
    use_case = ListSetsUseCase(set_repository)
    result = await use_case.execute(
        order=params.order,
        cursor=params.cursor,
        limit=params.limit,
    )
    return PaginatedResponseDTO[SetResponseDTO](
        items=[SetMapper.entity_to_response(set_) for set_ in result.items],
        next_cursor=result.next_cursor,
    )


@router.get(
    "/id/{id}",
    responses={
        404: NotFoundResponse,
        400: BadRequestResponse,
    },
)
async def get_set_by_id(
    id: str,
    set_repository: ISetRepository = Depends(get_set_repository),
    params: GetSetParams = Depends(),
) -> SetResponseDTO:
    use_case = GetSetUseCase(set_repository)
    result = await use_case.execute(id=id, add_set_type_info=params.add_set_type_info)

    return SetMapper.entity_to_response(result)


@router.get(
    "/code/{code}",
    responses={
        404: NotFoundResponse,
        400: BadRequestResponse,
    },
)
async def get_set_by_code(
    code: str,
    set_repository: ISetRepository = Depends(get_set_repository),
    params: GetSetParams = Depends(),
) -> SetResponseDTO:
    use_case = GetSetUseCase(set_repository)
    result = await use_case.execute(
        code=code, add_set_type_info=params.add_set_type_info
    )

    return SetMapper.entity_to_response(result)


@router.get(
    "/external_id/{external_id}",
    responses={
        404: NotFoundResponse,
        400: BadRequestResponse,
    },
)
async def get_set_by_external_id(
    external_id: str,
    set_repository: ISetRepository = Depends(get_set_repository),
    params: GetSetParams = Depends(),
) -> SetResponseDTO:
    use_case = GetSetUseCase(set_repository)
    result = await use_case.execute(
        external_id=external_id, add_set_type_info=params.add_set_type_info
    )

    return SetMapper.entity_to_response(result)
