from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_connection: mock.MagicMock) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        can_access_google_page("https://www.google.com")
        mocked_connection.assert_called_once()
        mocked_url.assert_called_once_with("https://www.google.com")
