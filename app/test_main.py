from unittest import mock
from app import main as app


def test_can_access_if_url_valid_and_has_connection() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url"
        ) as mock_valid_google_url,
        mock.patch(
            "app.main.has_internet_connection"
        ) as mock_has_internet_connections,
    ):
        mock_valid_google_url.return_value = True
        mock_has_internet_connections.return_value = True

        assert app.can_access_google_page(
            "https://google.com.ua") == "Accessible"


def test_can_access_if_url_valid_and_has_not_connection() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url"
        ) as mock_valid_google_url,
        mock.patch(
            "app.main.has_internet_connection"
        ) as mock_has_internet_connections,
    ):
        mock_valid_google_url.return_value = True
        mock_has_internet_connections.return_value = False

        assert app.can_access_google_page(
            "https://google.com.ua") == "Not accessible"


def test_can_access_if_url_not_valid_and_has_connection() -> None:
    with (
        mock.patch(
            "app.main.valid_google_url"
        ) as mock_valid_google_url,
        mock.patch(
            "app.main.has_internet_connection"
        ) as mock_has_internet_connections,
    ):
        mock_valid_google_url.return_value = False
        mock_has_internet_connections.return_value = True

        assert app.can_access_google_page(
            "https://google.com.ua") == "Not accessible"
