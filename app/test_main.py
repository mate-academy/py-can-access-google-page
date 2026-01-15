from unittest.mock import MagicMock, patch

from app.main import can_access_google_page
import pytest
from typing import Any


@pytest.fixture
def mock_valid_google_url() -> MagicMock:
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def mock_has_internet_connection() -> MagicMock:
    with patch("app.main.has_internet_connection") as mock:
        yield mock

def test_expected_access_google_page(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mock_valid_google_url.assert_called_once_with("https://www.google.com")
    mock_has_internet_connection.assert_called_once()


def test_invalid_time_connection(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_not_called()


def test_invalid_url(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mock_valid_google_url.assert_called_once_with("https://www.google.com")
    mock_has_internet_connection.assert_called_once()


def test_invalid_url_and_time_connection(
        mock_valid_google_url: Any,
        mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_not_called()
