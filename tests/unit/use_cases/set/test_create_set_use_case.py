from unittest.mock import AsyncMock

import pytest

from application.use_cases.set import CreateSetInput, CreateSetUseCase
from domain.entities import Set
from domain.exceptions import EntityAlreadyExistsError
from domain.ports.repositories import FindSetProps, ISetRepository

input_data = CreateSetInput(
    external_id="ext-123",
    code="tst1",
    name="Test Set",
    release_date="2024-01-01",
    card_count=100,
    is_foil=False,
    is_digital=False,
    is_foil_only=False,
    is_non_foil_only=False,
    set_type_id="set-type-uuid",
)


@pytest.mark.asyncio
async def test_create_set_use_case_raises_error_when_set_already_exists():
    # Arrange
    mock_repo = AsyncMock(spec=ISetRepository)

    # O repositório irá retornar um set existente
    mock_repo.get_by.return_value = Set(**input_data.model_dump())

    use_case = CreateSetUseCase(mock_repo)

    # Act + Assert
    with pytest.raises(EntityAlreadyExistsError) as exc:
        await use_case.execute(input_data)

    assert "tst1" in str(exc.value)
    mock_repo.get_by.assert_called_once_with(FindSetProps(code="tst1"))
    mock_repo.create.assert_not_called()


@pytest.mark.asyncio
async def test_create_set_use_case_creates_new_set_successfully():
    # Arrange
    mock_repo = AsyncMock(spec=ISetRepository)

    # Nenhum set encontrado
    mock_repo.get_by.return_value = None

    # ID que o repositório retornará
    mock_repo.create.return_value = "generated-uuid"

    use_case = CreateSetUseCase(mock_repo)

    # Act
    created_id = await use_case.execute(input_data)

    # Assert
    assert created_id == "generated-uuid"

    # Verifica se buscou corretamente
    mock_repo.get_by.assert_called_once_with(FindSetProps(code="tst1"))

    # Verifica se chamou create com uma entidade Set
    args, _ = mock_repo.create.call_args
    created_entity = args[0]
    assert isinstance(created_entity, Set)
    assert created_entity.code == "tst1"
    assert created_entity.name == "Test Set"
