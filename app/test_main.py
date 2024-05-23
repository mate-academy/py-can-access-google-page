from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accsesible() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection,
          mock.patch("app.main.valid_google_url")
          as mock_valid_google_url):

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        can_access_google_page("Test")

        mock_has_internet_connection.assert_called_once()
        mock_valid_google_url.assert_called_once_with("Test")

        assert can_access_google_page("") == "Accessible"


def test_can_access_google_page_not_accsesible() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection,
          mock.patch("app.main.valid_google_url")
          as mock_valid_google_url):

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False

        can_access_google_page("")

        assert can_access_google_page("") == "Not accessible"
