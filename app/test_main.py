from unittest import mock

from app.main import can_access_google_page

@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_has_been_called(mocked_valid_google_url, mocked_has_internet_connection):
    can_access_google_page("url")
    mocked_valid_google_url.assert_called_once()

    can_access_google_page("url")
    mocked_has_internet_connection.assert_called()
