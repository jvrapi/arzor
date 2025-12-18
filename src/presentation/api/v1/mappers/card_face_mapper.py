from application.use_cases.card import CreateCardFaceInput
from presentation.api.v1.schemas import CardFaceResponseDTO, CreateCardFaceDTO


class CardFaceMapper:
    @staticmethod
    def dto_to_input(dto: CreateCardFaceDTO) -> CreateCardFaceInput:
        # Usa o próprio pydantic para converter
        return CreateCardFaceInput(**dto.model_dump())

    @staticmethod
    def entity_to_response(entity) -> CardFaceResponseDTO:
        return CardFaceResponseDTO(
            id=entity.id,
            card_id=entity.card_id,
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
            image_uris=entity.image_uris,
            oracle_id=entity.oracle_id,
        )
