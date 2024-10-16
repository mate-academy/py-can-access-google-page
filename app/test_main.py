from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_should_valid_google_url(mocked_url):
    can_access_google_page("http://google.com")
    mocked_url.assert_called_once()

@mock.patch("app.main.has_internet_connection")
def test_should_has_internet_connection(mocked_connection):
    can_access_google_page("http://google.com")
    mocked_connection.assert_called_once()
