from fastapi import APIRouter, Depends

from application.use_cases.set_types import ListSetTypesUseCase
from domain.ports.repositories import ISetTypeRepository
from presentation.api.dependencies import get_set_type_repository
from presentation.api.v1.schemas.set import SetTypeResponseDTO

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
    # Implementation for creating a set would go here
