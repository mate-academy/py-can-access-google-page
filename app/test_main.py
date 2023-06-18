import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Connection allowed"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Connection denied because no internet connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Connection denied because url is not valid"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_connect(
        mocked_connection: Callable,
        mocked_valid_url: Callable,
        is_valid_url: bool,
        is_connected: bool,
        expected: str
) -> None:
    mocked_connection.return_value = is_connected
    mocked_valid_url.return_value = is_valid_url
    assert can_access_google_page("url") == expected
