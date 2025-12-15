from application.use_cases.card import CreateCardFaceInput
from presentation.api.v1.schemas import CreateCardFaceDTO


class CardFaceMapper:
    @staticmethod
    def dto_to_input(dto: CreateCardFaceDTO) -> CreateCardFaceInput:
        # Usa o próprio pydantic para converter
        return CreateCardFaceInput(**dto.model_dump())
