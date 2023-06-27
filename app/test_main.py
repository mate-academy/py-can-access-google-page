from typing import Any
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_return, has_connection_return, url, expected_result",
    [
        (True, True, "http://google.com", "Accessible"),
        (True, False, "http://google.com", "Not accessible"),
        (False, False, "http://google.com", "Not accessible"),
        (True, True, "http://pinterest.com", "Accessible"),
        (False, True, "http://rozetka.com.ua", "Not accessible"),
        (False, False, "http://rozetka.com.ua", "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_has_connection_and_valid_url(
        mocked_has_connection: Any,
        mocked_valid_url: Any,
        valid_url_return: bool,
        has_connection_return: bool,
        url: str,
        expected_result: str
) -> None:
    mocked_valid_url.return_value = valid_url_return
    mocked_has_connection.return_value = has_connection_return
    can_access = can_access_google_page(url)

    assert can_access == expected_result
