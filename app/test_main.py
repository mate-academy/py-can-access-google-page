from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_if_valid_google_url_was_called(mocked_valid_google_url: Any) -> None:
    can_access_google_page("http://google.com")
    mocked_valid_google_url.assert_called_once_with("http://google.com")


def test_if_has_internet_connection_was_called() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_internet_con:
        can_access_google_page("http://google.com")
        mocked_internet_con.assert_called_once()
