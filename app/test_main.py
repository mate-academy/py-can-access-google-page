from unittest.mock import patch, MagicMock
import pytest

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_url() -> MagicMock:
    with patch("app.main.valid_google_url") as mock_valid:
        yield mock_valid


@pytest.fixture
def mock_has_internet_connection() -> MagicMock:
    with patch("app.main.has_internet_connection") as mock_internet_connection:
        yield mock_internet_connection


def test_accessible_when_valid_url_and_internet(
    mock_valid_url: MagicMock, mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


def test_not_accessible_when_valid_url_no_internet(
    mock_valid_url: MagicMock, mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_when_invalid_url_and_internet(
    mock_valid_url: MagicMock, mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_not_accessible_when_invalid_url_and_no_internet(
    mock_valid_url: MagicMock, mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
