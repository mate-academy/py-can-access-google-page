from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_has_connection, mock_is_valid_url, url, expected",
    [
        pytest.param(
            True,
            True,
            "https://github.com/Kirontiko/",
            "Accessible",
            id="accessible when has connection and url is valid"
        ),
        pytest.param(
            False,
            True,
            "https://github.com/Kirontiko/",
            "Not accessible",
            id="not accessible when has no connection"
        ),
        pytest.param(
            True,
            False,
            "https://gitmug.com/3140,Kirontiko/",
            "Not accessible",
            id="not accessible when url is not valid"
        ),
        pytest.param(
            False,
            False,
            "https://gitmug.com/314-K,l;.irontiko/",
            "Not accessible",
            id="not accessible when url is not valid and no connection"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        has_internet_connection: Callable,
        valid_google_url: Callable,
        mock_has_connection: bool,
        mock_is_valid_url: bool,
        url: str,
        expected: str
) -> None:
    has_internet_connection.return_value = mock_has_connection
    valid_google_url.return_value = mock_is_valid_url
    assert can_access_google_page(url) == expected
