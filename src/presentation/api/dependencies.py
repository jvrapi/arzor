from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from domain.ports.repositories import ISetTypeRepository
from infra.database.base import get_db
from infra.database.repositories import SetRepository, SetTypeRepository


async def get_set_type_repository(
    session: AsyncSession = Depends(get_db),
) -> ISetTypeRepository:
    return SetTypeRepository(session)


async def get_set_repository(
    session: AsyncSession = Depends(get_db),
) -> ISetTypeRepository:
    return SetRepository(session)
