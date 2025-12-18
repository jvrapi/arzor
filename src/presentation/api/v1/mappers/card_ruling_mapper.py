from application.use_cases.card import CreateCardRulingInput
from presentation.api.v1.schemas import CreateCardRulingDTO


class CardRulingMapper:
    @staticmethod
    def dto_to_input(dto: CreateCardRulingDTO) -> CreateCardRulingInput:
        base_data = dto.model_dump()

        return CreateCardRulingInput(
            **base_data,
        )
