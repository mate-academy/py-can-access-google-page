from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_url(mocked_valid_url: callable) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_valid_url.assert_called_once_with("https://www.google.com/")


@mock.patch("app.main.has_internet_connection")
def test_connection_exists(mocked_connection: callable) -> None:
    can_access_google_page("https://www.google.com/")
    mocked_connection.assert_called_once()
