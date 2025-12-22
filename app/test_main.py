from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_validity
    ):
        url = "test"
        can_access_google_page(url)
        mock_connection.assert_called_once()
        mock_validity.assert_called_once_with(url)
