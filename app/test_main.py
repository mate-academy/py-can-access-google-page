from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, value_connection, value_validator, result, error",
    [
        (
            "https://www.google.com",
            True,
            True,
            "Accessible",
            "Function should return "
            "`Accessible` if all function passed."
        ),
        (
            "google.com",
            False,
            True,
            "Not accessible",
            "Function should return "
            "`Not accessible` if url doesn't valid."
        ),
        (
            "https://www.google.com",
            True,
            False,
            "Not accessible",
            "Function should return `Not accessible` "
            "If no connection."
        )
    ]
)
@mock.patch("app.main.valid_google_url", create=True)
@mock.patch("app.main.has_internet_connection", create=True)
def test_return_can_access_google_page(
        mocked_connection: Callable,
        mocked_validator: Callable,
        url: str,
        value_validator: bool,
        value_connection: bool,
        result: str,
        error: str,
) -> None:
    mocked_validator.return_value = value_validator
    mocked_connection.return_value = value_connection

    result_function = can_access_google_page(url)

    assert result_function == result, error
