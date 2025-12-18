from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import CardRuling
from domain.ports.repositories import ICardRulingRepository
from infra.database.models import CardRulingModel


class CardRulingRepository(ICardRulingRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_many(self, rulings: list[CardRuling]) -> list[str]:
        ids = []

        async with self._session.begin():
            for ruling in rulings:
                ruling_model = CardRulingModel(
                    card_id=ruling.card_id,
                    published_at=ruling.published_at,
                    comment=ruling.comment,
                    source=ruling.source,
                )

                self._session.add(ruling_model)

                await self._session.flush()

                ids.append(ruling_model.id)

        return ids
