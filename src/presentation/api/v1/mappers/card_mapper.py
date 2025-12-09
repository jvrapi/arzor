from application.use_cases.card import CreateCardInput
from presentation.api.v1.schemas import CreateCardDTO


class CardMapper:
    @staticmethod
    def dto_to_input(dto: CreateCardDTO) -> CreateCardInput:
        # Usa o próprio pydantic para converter
        return CreateCardInput(**dto.model_dump())
