from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection,
          mock.patch("app.main.valid_google_url")
          as mock_valid_google_url):

        url = "http://google.com"

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        assert can_access_google_page(url) == "Accessible"

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        assert can_access_google_page(url) == "Not accessible"

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        assert can_access_google_page(url) == "Not accessible"

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        assert can_access_google_page(url) == "Not accessible"

        mock_has_internet_connection.assert_has_calls()
        mock_valid_google_url.assert_has_calls()
