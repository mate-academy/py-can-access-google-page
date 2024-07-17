from typing import Any
from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "internet_connection_value, valid_google_url_value, url, expected_return",
    [
        pytest.param(
            True, True, "url", "Accessible",
            id="return 'accessible'"
        ),

        pytest.param(
            False, True, "new url", "Not accessible",
            id="return 'not accessible' because of internet connection"
        ),

        pytest.param(
            True, False, "invalid@", "Not accessible",
            id="return 'not accessible' because of invalid google url"
        ),
    ]
)
def test_can_access_google_page(
        mocked_internet_connection: Any,
        mocked_valid_google_url: Any,
        internet_connection_value: bool,
        valid_google_url_value: bool,
        url: str,
        expected_return: str
) -> None:
    mocked_internet_connection.return_value = internet_connection_value
    mocked_valid_google_url.return_value = valid_google_url_value

    assert can_access_google_page(url) == expected_return
