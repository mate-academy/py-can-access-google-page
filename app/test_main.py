import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_func:
        yield mock_func


@pytest.fixture
def mock_has_internet_connection() -> MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_func:
        yield mock_func


def test_can_access_google_page_accessible(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    url = "https://www.google.com"
    assert can_access_google_page(url) == "Accessible"


def test_can_access_google_page_no_internet(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    url = "https://www.google.com"
    assert can_access_google_page(url) == "Not accessible"


def test_can_access_google_page_invalid_url(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    url = "https://www.invalid-url.com"
    assert can_access_google_page(url) == "Not accessible"
