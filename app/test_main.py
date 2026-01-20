from typing import Callable

import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, is_valid, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),

    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: Callable,
        mocked_valid_google_url: Callable,
        has_internet: bool,
        is_valid: bool,
        result: str
) -> None:
    mocked_has_internet_connection.return_value = has_internet
    mocked_valid_google_url.return_value = is_valid
    assert can_access_google_page("url") == result
