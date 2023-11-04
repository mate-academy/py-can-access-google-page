from unittest import mock

from .main import can_access_google_page


def test_can_access_google_page() -> None:
    valid_google_url = "app.main.valid_google_url"
    has_internet_con = "app.main.has_internet_connection"
    with (mock.patch(valid_google_url) as mocked_valid_google_url,
          mock.patch(has_internet_con) as mocked_has_internet_connection):
        url = "https://www.google.com"
        assert can_access_google_page(url) == "Accessible"
        mocked_valid_google_url.assert_called_once_with(url)
        mocked_has_internet_connection.assert_called_once()
