from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import Card
from domain.ports.repositories import ICardRepository
from infra.database.models import CardModel


class CardRepository(ICardRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_many(self, cards: list[Card]) -> list[str]:
        models: list[CardModel] = []

        for card in cards:
            model = CardModel(
                set_id=card.set_id,
                external_id=card.external_id,
                oracle_id=card.oracle_id,
                name=card.name,
                lang=card.lang,
                released_at=card.released_at,
                layout=card.layout,
                image_uris=card.image_uris,
                cmc=card.cmc,
                type_line=card.type_line,
                oracle_text=card.oracle_text,
                mana_cost=card.mana_cost,
                power=card.power,
                toughness=card.toughness,
                loyalty=card.loyalty,
                colors=card.colors,
                color_identity=card.color_identity,
                keywords=card.keywords,
                legalities=card.legalities,
                collector_number=card.collector_number,
                rarity=card.rarity,
                border_color=card.border_color,
                security_stamp=card.security_stamp,
                finishes=card.finishes,
                is_reserved=card.is_reserved,
                is_game_changer=card.is_game_changer,
                is_foil=card.is_foil,
                is_non_foil=card.is_non_foil,
                is_oversized=card.is_oversized,
                is_promo=card.is_promo,
                is_reprint=card.is_reprint,
                is_variation=card.is_variation,
                is_full_art=card.is_full_art,
                is_textless=card.is_textless,
                is_found_on_booster=card.is_found_on_booster,
            )

            models.append(model)
            self._session.add(model)

        await self._session.commit()

        return [m.id for m in models]
