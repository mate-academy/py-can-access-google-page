from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        has_internet_connection: MagicMock,
        valid_google_url: MagicMock
) -> None:
    can_access_google_page("https://www.google.com")
    has_internet_connection.assert_called_once()
    valid_google_url.assert_called_once_with("https://www.google.com")
