from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        can_access_google_page("url")
        mocked_url.assert_called_once()
        mocked_connection.assert_called_once()
