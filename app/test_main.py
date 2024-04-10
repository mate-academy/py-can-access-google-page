from unittest import mock
from app.main import can_access_google_page


def test_has_internet_connection_was_called() -> None:
    with mock.patch(
            "app.main.has_internet_connection") as mocked_has_connection, \
            mock.patch("app.main.valid_google_url") as mocked_valid_url:
        url = "https://www.google.com"
        can_access_google_page(url)
        mocked_has_connection.assert_called_once()
        mocked_valid_url.assert_called_once()
