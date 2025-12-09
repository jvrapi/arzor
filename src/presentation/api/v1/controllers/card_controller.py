from fastapi import APIRouter, Depends, status

from application.use_cases.card import CreateCardUseCase
from domain.ports.repositories import ICardRepository
from presentation.api.dependencies import get_card_repository
from presentation.api.v1.mappers import CardMapper
from presentation.api.v1.schemas import CreateCardDTO, CreateCardResponseDTO

router = APIRouter(tags=["card"], prefix="/cards")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_card(
    cards: list[CreateCardDTO],
    card_repository: ICardRepository = Depends(get_card_repository),
) -> list[CreateCardResponseDTO]:
    create_card_use_case = CreateCardUseCase(card_repository=card_repository)

    created_ids = await create_card_use_case.execute(
        inputs=[CardMapper.dto_to_input(card) for card in cards]
    )
    return [{"id": id} for id in created_ids]
