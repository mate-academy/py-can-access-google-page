import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.fixture
def mock_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as mock:
        yield mock


@pytest.fixture
def mock_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as mock:
        yield mock


def test_when_no_internet_connection(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock) -> None:

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_when_not_valid_google_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock) -> None:

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_when_has_internet_and_valid_google_url(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock) -> None:

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"
