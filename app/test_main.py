from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    url = "http://google.com"

    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        can_access_google_page(url)
        mock_valid_google_url.assert_called_once_with(url)
        mock_has_internet_connection.assert_called_once()
