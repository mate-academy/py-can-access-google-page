from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mocked_url_validator: mock.MagicMock,
        mocked_internet_connection: mock.MagicMock
) -> None:
    url = "test.url/"
    can_access_google_page(url)
    mocked_url_validator.assert_called_once_with(url)
    mocked_internet_connection.assert_called()
