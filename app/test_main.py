import pytest

from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected_message",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test access if valid url and has connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test access if not valid url and has connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test access if valid url and has not connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="test access if not valid url and has not connection"
        )
    ]
)
def test_can_access_if_has_connection_and_valid_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_message: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    assert can_access_google_page("url") == expected_message
