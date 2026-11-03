from collections.abc import Callable
from datetime import datetime
from unittest.mock import Mock

import pytest
from pytest import MonkeyPatch

from app import main


@pytest.fixture
def mock_current_time(monkeypatch: MonkeyPatch) -> Callable:
    def _mock_current_time(
        hour: int,
        minute: int,
        second: int,
    ) -> None:
        mock_datetime = Mock()
        mock_datetime.now.return_value = datetime(
            2026, 1, 1, hour, minute, second
        )

        monkeypatch.setattr(main.datetime, "datetime", mock_datetime)

    return _mock_current_time


@pytest.mark.parametrize(
    ("has_internet", "is_valid_url", "expected"),
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch,
    has_internet: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: has_internet,
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: is_valid_url,
    )

    assert main.can_access_google_page("https://google.com") == expected


@pytest.mark.parametrize(
    ("hour", "minute", "second", "expected"),
    [
        (6, 0, 0, True),
        (22, 59, 59, True),
        (5, 59, 59, False),
        (23, 0, 0, False),
    ],
)
def test_has_internet_connection(
    mock_current_time: Callable,
    hour: int,
    minute: int,
    second: int,
    expected: bool,
) -> None:
    mock_current_time(hour, minute, second)

    assert main.has_internet_connection() is expected
