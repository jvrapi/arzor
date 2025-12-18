from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from domain.ports.repositories import (
    ICardRepository,
    ICardRulingRepository,
    ISetTypeRepository,
)
from infra.database.base import get_db
from infra.database.repositories import (
    CardRepository,
    CardRulingRepository,
    SetRepository,
    SetTypeRepository,
)


async def get_set_type_repository(
    session: AsyncSession = Depends(get_db),
) -> ISetTypeRepository:
    return SetTypeRepository(session)


async def get_set_repository(
    session: AsyncSession = Depends(get_db),
) -> ISetTypeRepository:
    return SetRepository(session)


async def get_card_repository(
    session: AsyncSession = Depends(get_db),
) -> ICardRepository:
    return CardRepository(session)


async def get_card_ruling_repository(
    session: AsyncSession = Depends(get_db),
) -> ICardRulingRepository:
    return CardRulingRepository(session)
