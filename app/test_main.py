from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_exist(
        mocked_connection: MagicMock, mocked_url: MagicMock
) -> None:
    can_access_google_page("http://google.com")
    mocked_connection.assert_called_once()
    mocked_url.assert_called_once()
