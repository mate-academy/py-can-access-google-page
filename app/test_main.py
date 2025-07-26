from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_connection: Any, mocked_url: Any) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True

    result = can_access_google_page("url")
    mocked_url.assert_called_once_with("url")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
def test_cannot_access_google_page(mocked_connection: Any) -> None:
    mocked_connection.return_value = False

    result = can_access_google_page("url")
    assert result == "Not accessible"
