from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection
        ) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        can_access_google_page("https://www.google.com/")
        mocked_has_internet_connection.assert_called_once()
        mocked_valid_google_url.assert_called_once_with("https://www.google.com/")
