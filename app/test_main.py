from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(has_internet_connection: Any,
                                valid_google_url: Any) -> None:

    url = "https://google.com/"
    assert can_access_google_page(url) == "Accessible"
    has_internet_connection.assert_called_once()
    valid_google_url.assert_called_once_with(url)
