from unittest import mock

from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(valid_url: Any, has_connection: Any) -> None:
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Accessible"
    has_connection.assert_called_once()
    valid_url.assert_called_once_with(url)
