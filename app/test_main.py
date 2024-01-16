from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_connection: callable,
                                mock_validator: callable) -> None:
    url = "http://google.com"

    can_access_google_page(url)

    mock_validator.assert_called_once_with(url)
    mock_connection.assert_any_call()
