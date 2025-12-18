from application.use_cases.set import CreateSetInput
from domain.entities.set import Set
from presentation.api.v1.schemas import CreateSetDTO, SetResponseDTO, SetTypeResponseDTO


class SetMapper:
    @staticmethod
    def dto_to_input(dto: CreateSetDTO) -> CreateSetInput:
        base_data = dto.model_dump()

        return CreateSetInput(
            **base_data,
        )

    @staticmethod
    def entity_to_response(entity: Set) -> SetResponseDTO:
        return SetResponseDTO(
            id=entity.id,
            name=entity.name,
            code=entity.code,
            external_id=entity.external_id,
            set_type_id=entity.set_type_id,
            card_count=entity.card_count,
            release_date=entity.release_date,
            is_digital=entity.is_digital,
            is_foil_only=entity.is_foil_only,
            is_nonfoil_only=entity.is_nonfoil_only,
            icon_uri=entity.icon_uri,
            set_type=SetTypeResponseDTO(
                description=entity.set_type.description,
                id=entity.set_type.id,
                name=entity.set_type.name,
            )
            if entity.set_type
            else None,
        )
