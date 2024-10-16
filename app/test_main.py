from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_exist(mocked_url: Any) -> None:
    can_access_google_page("http://google.com")
    mocked_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_exist(mocked_connection: Any) -> None:
    can_access_google_page("http://google.com")
    mocked_connection.assert_called_once()
