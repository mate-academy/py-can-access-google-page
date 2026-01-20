from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


TEST_URL = "https://github.com/Kirontiko/"


@pytest.mark.parametrize(
    "mock_has_connection, mock_is_valid_url, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="accessible when has connection and url is valid"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="not accessible when has no connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="not accessible when url is not valid"
        ),
        pytest.param(
            False,
            False,
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
        expected: str
) -> None:
    has_internet_connection.return_value = mock_has_connection
    valid_google_url.return_value = mock_is_valid_url
    assert can_access_google_page(TEST_URL) == expected
