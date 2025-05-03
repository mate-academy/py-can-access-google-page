from app.main import can_access_google_page as google_page
from unittest import mock


def test_valid_url_and_connection_exists() -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_url,
          mock.patch("app.main.has_internet_connection") as mocked_connect):
        assert google_page("https://www.google.com/") == "Accessible"
        mocked_valid_url.assert_called_once_with("https://www.google.com/")
        mocked_connect.assert_called_once()
