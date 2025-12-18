from sqlalchemy import inspect

from domain.entities import Card, CardFace
from infra.database.models import CardFaceModel, CardModel

from .set_mapper import SetMapper


class CardMapper:
    @staticmethod
    def to_entity(model: CardModel) -> Card:
        state = inspect(model)

        set_entity = None
        if "set" not in state.unloaded:
            if model.set:
                set_entity = SetMapper.to_entity(model.set)

        return Card(
            id=model.id,
            external_id=model.external_id,
            set_id=model.set_id,
            oracle_id=model.oracle_id,
            name=model.name,
            lang=model.lang,
            released_at=model.released_at,
            layout=model.layout,
            image_uris=model.image_uris,
            collector_number=model.collector_number,
            rarity=model.rarity,
            border_color=model.border_color,
            security_stamp=model.security_stamp,
            finishes=model.finishes,
            is_reserved=model.is_reserved,
            is_game_changer=model.is_game_changer,
            is_oversized=model.is_oversized,
            is_promo=model.is_promo,
            is_reprint=model.is_reprint,
            is_variation=model.is_variation,
            is_full_art=model.is_full_art,
            is_textless=model.is_textless,
            is_found_on_booster=model.is_found_on_booster,
            mana_cost=model.mana_cost,
            cmc=model.cmc,
            type_line=model.type_line,
            oracle_text=model.oracle_text,
            power=model.power,
            toughness=model.toughness,
            loyalty=model.loyalty,
            colors=model.colors,
            color_identity=model.color_identity,
            keywords=model.keywords,
            legalities=model.legalities,
            set=set_entity,
            faces=[CardFaceMapper.to_entity(face) for face in model.faces]
            if model.faces
            else [],
        )


class CardFaceMapper:
    @staticmethod
    def to_entity(model: CardFaceModel) -> CardFace:
        return CardFace(
            id=model.id,
            card_id=model.card_id,
            name=model.name,
            oracle_id=model.oracle_id,
            mana_cost=model.mana_cost,
            type_line=model.type_line,
            oracle_text=model.oracle_text,
            power=model.power,
            toughness=model.toughness,
            loyalty=model.loyalty,
            colors=model.colors,
            color_identity=model.color_identity,
            cmc=model.cmc,
            image_uris=model.image_uris,
        )
