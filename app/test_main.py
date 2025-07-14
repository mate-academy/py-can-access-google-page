from unittest.mock import patch, Mock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_call_valid_google_url_and_has_internet_connection(
        mocked_internet_connection: Mock,
        mocked_google_url: Mock
) -> None:
    can_access_google_page("www.google.com")
    mocked_internet_connection.assert_called_once()
    mocked_google_url.assert_called_once_with("www.google.com")
