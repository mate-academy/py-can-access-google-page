from unittest.mock import patch, Mock, MagicMock
from .main import (can_access_google_page,
                   has_internet_connection,
                   valid_google_url)


def test_valid_google_url() -> None:
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        assert valid_google_url("https://www.google.com/") is True


def test_valid_google_url_failure() -> None:
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        assert valid_google_url("https://www.google.com/") is False


def test_has_internet_connection_daytime() -> None:
    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock()
        mock_now.hour = 12
        mock_datetime.now.return_value = mock_now
        assert has_internet_connection() is True


def test_has_internet_connection_nighttime() -> None:
    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock()
        mock_now.hour = 2
        mock_datetime.now.return_value = mock_now
        assert has_internet_connection() is False


def test_can_access_google_page_accessible() -> None:
    with (patch("app.main.has_internet_connection") as mock_has_internet,
          patch("app.main.valid_google_url") as mock_valid_url):
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Accessible"


def test_can_access_google_page_not_accessible() -> None:
    with (patch("app.main.has_internet_connection") as mock_has_internet,
          patch("app.main.valid_google_url") as mock_valid_url):
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"


def test_can_access_google_page_invalid_url() -> None:
    with (patch("app.main.has_internet_connection") as mock_has_internet,
          patch("app.main.valid_google_url") as mock_valid_url):
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        assert can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"
