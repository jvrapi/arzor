from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities import Card
from domain.ports.repositories import ICardRepository
from infra.database.models import CardFaceModel, CardModel


class CardRepository(ICardRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_many(self, cards: list[Card]) -> list[str]:
        ids = []

        async with self._session.begin():
            for card in cards:
                card_model = CardModel(
                    external_id=card.external_id,
                    set_id=card.set_id,
                    oracle_id=card.oracle_id,
                    name=card.name,
                    lang=card.lang,
                    released_at=card.released_at,
                    layout=card.layout,
                    image_uris=card.image_uris,
                    collector_number=card.collector_number,
                    rarity=card.rarity,
                    border_color=card.border_color,
                    security_stamp=card.security_stamp,
                    finishes=card.finishes,
                    is_reserved=card.is_reserved,
                    is_game_changer=card.is_game_changer,
                    is_oversized=card.is_oversized,
                    is_promo=card.is_promo,
                    is_reprint=card.is_reprint,
                    is_variation=card.is_variation,
                    is_full_art=card.is_full_art,
                    is_textless=card.is_textless,
                    is_found_on_booster=card.is_found_on_booster,
                    mana_cost=card.mana_cost,
                    cmc=card.cmc,
                    type_line=card.type_line,
                    oracle_text=card.oracle_text,
                    power=card.power,
                    toughness=card.toughness,
                    loyalty=card.loyalty,
                    colors=card.colors,
                    color_identity=card.color_identity,
                    keywords=card.keywords,
                    legalities=card.legalities,
                )

                self._session.add(card_model)

                await self._session.flush()

                for face in card.faces:
                    face_model = CardFaceModel(
                        card_id=card_model.id,
                        name=face.name,
                        oracle_id=face.oracle_id,
                        mana_cost=face.mana_cost,
                        type_line=face.type_line,
                        oracle_text=face.oracle_text,
                        power=face.power,
                        toughness=face.toughness,
                        loyalty=face.loyalty,
                        colors=face.colors,
                        color_identity=face.color_identity,
                        cmc=face.cmc,
                        image_uris=({**face.image_uris} if face.image_uris else None),
                    )

                    self._session.add(face_model)

                ids.append(card_model.id)

        return ids
