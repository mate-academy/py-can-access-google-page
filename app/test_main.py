from app.main import valid_google_url, has_internet_connection, \
    can_access_google_page
from unittest import mock

def test_can_access_google_page():
    with mock.patch("valid_google_url") as mock_valid_google_url, \
            mock.patch("has_internet_connection") as \
                    mock_has_internet_connection:

        can_access_google_page("https://www.google.pl/?hl=pl")
        mock_valid_google_url.assert_called_once_with("https://www.google.pl/?hl=pl")
        mock_has_internet_connection.assert_called_once()


