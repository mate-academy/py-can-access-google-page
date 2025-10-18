from unittest import mock
from app.main import *


def test_can_access_google_page_when_valid_url_and_connection_true() -> None:
    url = "https://www.google.com/?hl=ru"
    with (mock.patch("app.main.valid_google_url", return_value=True) as valid_url,
        mock.patch("app.main.has_internet_connection", return_value=True) as internet_connection,
    ):
        result = can_access_google_page(url)
        valid_url.assert_called_once_with(url)
        internet_connection.assert_called_once_with()
        assert result == "Accessible"

def test_can_access_google_page_when_valid_url_and_connection_false() -> None:
    url = "https://www.google.com/?hl=ru"
    with (mock.patch("app.main.has_internet_connection", return_value=False) as internet_connection,
          mock.patch("app.main.valid_google_url", return_value=False) as valid_url):
        result = can_access_google_page(url)
        internet_connection.assert_called_once_with()
        assert result == "Not accessible"

def test_can_access_google_page_when_invalid_url():
    url = "https://invalid.url"
    with (mock.patch("app.main.has_internet_connection", return_value=True) as internet_connection,
          mock.patch("app.main.valid_google_url", return_value=False) as valid_url):
        result = can_access_google_page(url)
        valid_url.assert_called_once_with(url)
        internet_connection.assert_called_once_with()
        assert result == "Not accessible"

def test_can_access_google_page_when_not_internet_connection() -> None:
    url = "https://www.google.com/?hl=ru"
    with mock.patch("app.main.has_internet_connection", return_value=False) as internet_connection:
        result = can_access_google_page(url)
        internet_connection.assert_called_once_with()
        assert result == "Not accessible"
