from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock
) -> None:
    can_access_google_page("https://www.google.com")
    mocked_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called_once()
