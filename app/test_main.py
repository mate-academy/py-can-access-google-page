import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> MagicMock:
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture()
def mock_has_internet_connection() -> MagicMock:
    with patch("app.main.has_internet_connection") as mock:
        yield mock


def test_can_access_google_page_valid_url(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("valid-url")
    assert result == "Accessible"


def test_can_access_google_page_invalid_url(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    result = can_access_google_page("invalid-url")
    assert result == "Not accessible"


def test_can_access_google_page_no_internet_and_valid_url(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("invalid-url")
    assert result == "Not accessible"


def test_cannot_access_if_only_valid_url(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    result = can_access_google_page("valid-url")
    assert result == "Not accessible"
