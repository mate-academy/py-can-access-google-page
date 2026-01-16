from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_valid_url: MagicMock,
        mocked_has_connection: MagicMock) -> None:
    mocked_valid_url.return_value = True
    mocked_has_connection.return_value = True

    assert can_access_google_page("https//:www.google.com") == "Accessible"

    mocked_valid_url.assert_called()
    mocked_has_connection.assert_called()
