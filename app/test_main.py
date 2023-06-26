from typing import Any
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_connection_and_valid_url(
        mocked_has_connection: Any,
        mocked_valid_url: Any
) -> None:

    url = "http://google.com"
    can_access = can_access_google_page(url)

    mocked_has_connection.assert_called()
    mocked_valid_url.assert_called_once_with(url)

    assert can_access == "Accessible"
