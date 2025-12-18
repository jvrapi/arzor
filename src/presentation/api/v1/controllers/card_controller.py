from fastapi import APIRouter, Depends, status

from application.use_cases.card import CreateCardRulingsUseCase, CreateCardUseCase
from domain.ports.repositories import ICardRepository, ICardRulingRepository
from presentation.api.dependencies import (
    get_card_repository,
    get_card_ruling_repository,
)
from presentation.api.v1.mappers import CardMapper, CardRulingMapper
from presentation.api.v1.schemas import (
    CardRulingResponseDTO,
    CreateCardDTO,
    CreateCardResponseDTO,
    CreateCardRulingDTO,
)

router = APIRouter(tags=["Card"], prefix="/cards")


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


@router.post("/rulings", status_code=status.HTTP_201_CREATED)
async def create_card_rulings(
    rulings: list[CreateCardRulingDTO],
    card_ruling_repository: ICardRulingRepository = Depends(get_card_ruling_repository),
) -> list[CardRulingResponseDTO]:
    usecase = CreateCardRulingsUseCase(card_ruling_repository)
    created_ids = await usecase.execute(
        [CardRulingMapper.dto_to_input(ruling) for ruling in rulings]
    )

    return [{"id": id} for id in created_ids]
