from application.use_cases.card import CreateCardInput
from domain.entities.card import Card
from presentation.api.v1.schemas import (
    CardResponseDTO,
    CreateCardDTO,
)

from .card_face_mapper import CardFaceMapper
from .set_mapper import SetMapper


class CardMapper:
    @staticmethod
    def dto_to_input(dto: CreateCardDTO) -> CreateCardInput:
        base_data = dto.model_dump(exclude={"faces"})

        return CreateCardInput(
            **base_data,
            faces=[CardFaceMapper.dto_to_input(face_dto) for face_dto in dto.faces]
            if dto.faces
            else [],
        )

    @staticmethod
    def entity_to_response(entity: Card) -> CardResponseDTO:
        return CardResponseDTO(
            id=entity.id,
            set_id=entity.set_id,
            name=entity.name,
            mana_cost=entity.mana_cost,
            cmc=entity.cmc,
            type_line=entity.type_line,
            oracle_text=entity.oracle_text,
            power=entity.power,
            toughness=entity.toughness,
            loyalty=entity.loyalty,
            colors=entity.colors,
            color_identity=entity.color_identity,
            rarity=entity.rarity,
            border_color=entity.border_color,
            security_stamp=entity.security_stamp,
            finishes=entity.finishes,
            is_reserved=entity.is_reserved,
            is_game_changer=entity.is_game_changer,
            is_oversized=entity.is_oversized,
            is_promo=entity.is_promo,
            is_reprint=entity.is_reprint,
            is_variation=entity.is_variation,
            is_full_art=entity.is_full_art,
            is_textless=entity.is_textless,
            is_found_on_booster=entity.is_found_on_booster,
            collector_number=entity.collector_number,
            external_id=entity.external_id,
            image_uris=entity.image_uris,
            keywords=entity.keywords,
            lang=entity.lang,
            layout=entity.layout,
            legalities=entity.legalities,
            oracle_id=entity.oracle_id,
            released_at=entity.released_at,
            set=SetMapper.entity_to_response(entity.set) if entity.set else None,
            faces=[CardFaceMapper.entity_to_response(face) for face in entity.faces]
            if entity.faces
            else None,
        )
