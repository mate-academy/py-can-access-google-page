from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
class TestCanAccessCase:
    def test_can_access_according_connections_and_valid_url(self, mock_has_internet_connection, mock_valid_google_url):
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        assert can_access_google_page('') == "Accessible"

    def test_cant_access_with_invalid_url(self, mock_has_internet_connection, mock_valid_google_url):
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        assert can_access_google_page('') == "Not accessible"

    def test_cant_access_without_internet_connection(self, mock_has_internet_connection, mock_valid_google_url):
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        assert can_access_google_page('') == "Not accessible"

    def test_cant_access_without_internet_connection_and_invalid_url(
            self, mock_has_internet_connection, mock_valid_google_url
    ):
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        assert can_access_google_page('') == "Not accessible"
