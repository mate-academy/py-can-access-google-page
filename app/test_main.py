from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page():
    with (patch("app.main.has_internet_connection") as mock_connection,
          patch("app.main.valid_google_url") as mock_valid_url):
        url = "https://google.com/"
        result = can_access_google_page(url)

        assert result == "Accessible"

        mock_connection.assert_called_once()
        mock_valid_url.assert_called_once_with(url)
