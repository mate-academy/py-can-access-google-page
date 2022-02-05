from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google(mocked_request, mocked_connection):
    mocked_request.return_value = True
    mocked_connection.return_value = True

    can_access_google_page("http://www.google.com")

    mocked_request.assert_called_once_with("http://www.google.com")
    mocked_connection.assert_called_once()
