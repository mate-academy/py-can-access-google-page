import pytest

from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "can_access,is_valid,connection_status",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="It must be correct connection if user has internet connection "
               "and valid URL"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="It mustn't be correct connection if user hasn't internet "
               "connection but has valid URL"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="It mustn't be correct connection if user has internet "
               "connection but don't has valid URL"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="It mustn't be correct connection if user hasn't internet "
               "connection and valid URL"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_correct_access(mocked_has_internet_connection: Callable,
                        mocked_valid_google_url: Callable,
                        can_access: bool,
                        is_valid: bool,
                        connection_status: str) -> None:

    mocked_has_internet_connection.return_value = can_access
    mocked_valid_google_url.return_value = is_valid

    assert can_access_google_page("some_url") == connection_status
