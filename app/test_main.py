import pytest
from unittest.mock import Mock, patch
from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture
def mock_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as mock_internet_connection:
        yield mock_internet_connection


def test_can_access_google_page_accessible(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    url = "https://www.google.com"
    result = can_access_google_page(url)

    assert result == "Accessible"


def test_can_access_google_page_not_accessible(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    url = "https://www.google.com"
    result = can_access_google_page(url)

    assert result == "Not accessible"


def test_can_access_google_page_invalid_url(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    url = "https://www.invalidurl.com"
    result = can_access_google_page(url)

    assert result == "Not accessible"


def test_can_access_google_page_invalid_url_and_no_internet(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    url = "https://www.invalidurl.com"
    result = can_access_google_page(url)

    assert result == "Not accessible"
