from typing import Any, Generator
from unittest.mock import MagicMock, AsyncMock

import pytest
from unittest import mock

from app.main import can_access_google_page


url = "test_url"


@pytest.fixture
def mock_validation() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch("app.main.valid_google_url") as mock_validation:
        yield mock_validation


@pytest.fixture
def mock_connection() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_valid_url_and_connection_exists(
        mock_validation: MagicMock,
        mock_connection: MagicMock,
) -> None:
    mock_validation.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page(url) == "Accessible"


def test_not_valid_url_and_connection_exists(
        mock_validation: MagicMock,
        mock_connection: MagicMock,
) -> None:
    mock_validation.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page(url) == "Not accessible"


def test__valid_url_and_connection_not_exists(
        mock_validation: MagicMock,
        mock_connection: MagicMock,
) -> None:
    mock_validation.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"


def test_should_request_validation(
        mock_validation: MagicMock,
        mock_connection: MagicMock,
) -> None:
    can_access_google_page(url)
    mock_validation.assert_called_once_with(url)


def test_should_request_connection(
        mock_validation: MagicMock,
        mock_connection: MagicMock,
) -> None:
    can_access_google_page(url)
    mock_connection.assert_called_once()
