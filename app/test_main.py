import datetime
from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet: mock.MagicMock
        mock_valid_url: mock.MagicMock

        mock_internet.return_value = True
        mock_valid_url.return_value = True
        assert can_access_google_page("https://www.google.com") == "Accessible"

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        assert (
            can_access_google_page("https://www.google.com") =="Not accessible"
        )

        mock_internet.return_value = False
        mock_valid_url.return_value = True
        assert (
            can_access_google_page("https://www.google.com") == "Not accessible"
        )
