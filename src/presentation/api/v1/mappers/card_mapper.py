from application.use_cases.card import CreateCardInput
from presentation.api.v1.schemas import CreateCardDTO

from .card_face_mapper import CardFaceMapper


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
