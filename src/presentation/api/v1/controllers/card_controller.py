from fastapi import APIRouter, Depends, status

from application.use_cases.card import (
    CreateCardRulingsUseCase,
    CreateCardUseCase,
    ListCardsUseCase,
)
from domain.ports.repositories import ICardRepository, ICardRulingRepository
from presentation.api.dependencies import (
    get_card_repository,
    get_card_ruling_repository,
)
from presentation.api.v1.mappers import CardMapper, CardRulingMapper
from presentation.api.v1.schemas import (
    CardResponseDTO,
    CardRulingResponseDTO,
    CreateCardDTO,
    CreateCardResponseDTO,
    CreateCardRulingDTO,
    ListCardsParamsDTO,
    PaginatedResponseDTO,
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


@router.get("/")
async def list_cards(
    card_repository: ICardRepository = Depends(get_card_repository),
    params: ListCardsParamsDTO = Depends(),
) -> PaginatedResponseDTO[CardResponseDTO]:
    use_case = ListCardsUseCase(card_repository)
    result = await use_case.execute(**params.model_dump())

    return PaginatedResponseDTO[CardResponseDTO](
        items=[CardMapper.entity_to_response(card) for card in result.items],
        next_cursor=result.next_cursor,
    )
