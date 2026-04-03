from unittest import mock
from app.main import can_access_google_page


def test_access_when_url_and_connection_are_valid() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet: mock.MagicMock
        mock_valid_url: mock.MagicMock

        mock_internet.return_value = True
        mock_valid_url.return_value = True
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Accessible"


def test_no_access_when_url_is_invalid() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet: mock.MagicMock
        mock_valid_url: mock.MagicMock

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Not accessible"


def test_no_access_when_connection_is_missing() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet: mock.MagicMock
        mock_valid_url: mock.MagicMock

        mock_internet.return_value = False
        mock_valid_url.return_value = True
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Not accessible"
