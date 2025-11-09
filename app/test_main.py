from __future__ import annotations
import pytest
from unittest import mock
from unittest.mock import MagicMock, AsyncMock
from typing import Generator
from app.main import can_access_google_page


@pytest.fixture
def mock_url_validation() -> Generator[MagicMock | AsyncMock]:
    with mock.patch("app.main.valid_google_url") as mocked_url_validation:
        yield mocked_url_validation


@pytest.fixture
def mock_connection() -> Generator[MagicMock | AsyncMock]:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_returns_accessible_when_url_is_valid_and_is_connected(
        mock_connection: MagicMock | AsyncMock,
        mock_url_validation: MagicMock | AsyncMock
) -> None:
    mock_url_validation.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("url.com") == "Accessible"


def test_returns_not_accessible_when_url_is_valid_but_no_connection(
        mock_connection: mock.MagicMock | mock.AsyncMock,
        mock_url_validation: mock.MagicMock | mock.AsyncMock
) -> None:
    mock_url_validation.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"


def test_returns_not_accessible_when_is_connected_but_url_is_not_valid(
        mock_connection: mock.MagicMock | mock.AsyncMock,
        mock_url_validation: mock.MagicMock | mock.AsyncMock
) -> None:
    mock_url_validation.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible"


def test_returns_not_accessible_when_url_is_not_valid_and_no_connection(
        mock_connection: mock.MagicMock | mock.AsyncMock,
        mock_url_validation: mock.MagicMock | mock.AsyncMock
) -> None:
    mock_url_validation.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
