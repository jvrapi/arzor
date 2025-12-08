from datetime import datetime, timezone
from unittest.mock import AsyncMock

import pytest

from application.use_cases.set.list_sets_use_case import ListSetsUseCase
from domain.entities import Set
from domain.value_objects import PaginatedResult


def make_set(
    id: str = "1",
    set_type_id: str = "type_1",
):
    return Set(
        id=id,
        set_type_id=set_type_id,
        external_id="ext_123",
        code="SET1",
        name="Set Name",
        card_count=100,
        release_date=datetime(2024, 1, 1, tzinfo=timezone.utc),
        is_digital=False,
        is_foil_only=False,
        is_non_foil_only=False,
        icon_uri="https://example.com/icon.png",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        set_type=None,
    )


@pytest.mark.asyncio
async def test_list_sets_use_case():
    # Arrange
    mock_repository = AsyncMock()
    use_case = ListSetsUseCase(mock_repository)

    expected_result = PaginatedResult(
        items=[make_set("1"), make_set("2")],
        next_cursor="abc123",
    )

    mock_repository.list.return_value = expected_result

    # Act
    result = await use_case.execute(
        limit=5,
        cursor=None,
        order="asc",
    )

    # Assert
    mock_repository.list.assert_awaited_once_with(
        limit=5,
        cursor=None,
        order="asc",
    )

    assert result == expected_result
    assert len(result.items) == 2
    assert result.next_cursor == "abc123"


@pytest.mark.asyncio
async def test_list_sets_use_case_with_cursor_and_desc_order():
    # Arrange
    mock_repository = AsyncMock()
    use_case = ListSetsUseCase(mock_repository)

    expected_result = PaginatedResult(
        items=[],
        next_cursor=None,
    )

    mock_repository.list.return_value = expected_result

    # Act
    result = await use_case.execute(
        limit=10,
        cursor="cursor123",
        order="desc",
    )

    # Assert
    mock_repository.list.assert_awaited_once_with(
        limit=10,
        cursor="cursor123",
        order="desc",
    )

    assert result == expected_result
    assert result.items == []
    assert result.next_cursor is None
