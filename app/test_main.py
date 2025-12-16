from unittest import mock
from app.main import can_access_google_page


def test_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        mock_url.return_value = True


def test_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        mock_connection.return_value = True


def test_can_access_google_page() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        with mock.patch("app.main.has_internet_connection") as mock_connection:
            mock_url.return_value = True
            mock_connection.return_value = True
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"


def test_cannot_access_google_page_when_only_connection_is_true() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        with mock.patch("app.main.has_internet_connection") as mock_connection:
            mock_url.return_value = False
            mock_connection.return_value = True
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_cannot_access_google_page_when_only_url_is_true() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        with mock.patch("app.main.has_internet_connection") as mock_connection:
            mock_url.return_value = True
            mock_connection.return_value = False
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
