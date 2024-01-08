from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,has_connect,valid_url,result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://gmail.com", True, True, "Accessible"),
        ("https://bidadsxng.com", False, True, "Not accessible"),
        ("https://zvdadsxng.com", True, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: Callable,
        mocked_valid_url: Callable,
        url: str,
        has_connect: bool,
        valid_url: bool,
        result: str
) -> None:
    mocked_has_internet_connection.return_value = has_connect
    mocked_valid_url.return_value = valid_url
    assert can_access_google_page(url) == result
