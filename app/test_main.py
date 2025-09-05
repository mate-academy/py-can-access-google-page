from app.main import can_access_google_page
from unittest import mock


def test_site_is_accessible() -> None:
    url = "https://www.google.com/"

    with (
        mock.patch("app.main.valid_google_url") as mock_valid_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        can_access_google_page(url)
        mock_valid_url.assert_called_once_with(url)
        mock_has_connection.assert_called_once()
