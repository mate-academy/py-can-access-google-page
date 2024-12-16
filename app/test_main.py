from unittest.mock import patch
from typing import Callable

from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_connection_exists(
    valid: Callable, internet: Callable
) -> None:
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Accessible"
    valid.assert_called_once_with(url)
    internet.assert_called_once()
