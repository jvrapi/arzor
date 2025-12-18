from application.use_cases.set import CreateSetInput
from presentation.api.v1.schemas import CreateSetDTO


class SetMapper:
    @staticmethod
    def dto_to_input(dto: CreateSetDTO) -> CreateSetInput:
        base_data = dto.model_dump()

        return CreateSetInput(
            **base_data,
        )
