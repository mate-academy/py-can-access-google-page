import app.main
from app.main import can_access_google_page
from unittest import mock


def test_access_google_page_without_internet_connection() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=True)
    app.main.has_internet_connection = mock.MagicMock(return_value=False)
    assert can_access_google_page(
        "https://www.google.com.ua/") == "Not accessible"


def test_access_google_page_with_invalid_url() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=False)
    app.main.has_internet_connection = mock.MagicMock(return_value=True)
    assert can_access_google_page(
        "https://www.ggle.com.ua/") == "Not accessible"


def test_access_google_page_when_everything_is_good() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=True)
    app.main.has_internet_connection = mock.MagicMock(return_value=True)
    assert can_access_google_page("https://www.google.com.ua/") == "Accessible"
