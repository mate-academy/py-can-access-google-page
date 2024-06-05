from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (
        patch(
            "app.main.has_internet_connection"
        ) as mock_has_internet_connection,
        patch(
            "app.main.valid_google_url"
        ) as mock_valid_google_url
    ):
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        assert can_access_google_page("http://www.google.com") == "Accessible"

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        assert can_access_google_page(
            "http://www.google.com") == "Not accessible"
