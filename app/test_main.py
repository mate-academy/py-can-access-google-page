from unittest import mock
from app import main


def test_check_can_access_google_page() -> None:
    
    with (mock.patch("app.main.valid_google_url") as mock_url,
         mock.patch("app.main.has_internet_connection") as mock_connection):

        assert main.can_access_google_page("https://google.com")
        mock_url.assert_called_once()
        mock_connection.assert_called_once()
