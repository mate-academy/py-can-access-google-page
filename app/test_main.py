from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page

GOOGLE_URL = "https://www.google.com/"


@pytest.fixture
def patch_inner_functions() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked_url, \
         mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_url, mocked_connection


@pytest.mark.parametrize(
    "url_return_value, conn_return_value, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid_url_and_internet_connection",
        "not_accessible_without_valid_url",
        "not_accessible_without_connection",
        "not_accessible_without_valid_url_and_connection"
    ]
)
def test_should_return_correct_access(
        patch_inner_functions: Callable,
        url_return_value: bool,
        conn_return_value: bool,
        expected_result: str
) -> None:
    mock_url, mock_connection = patch_inner_functions

    mock_url.return_value = url_return_value
    mock_connection.return_value = conn_return_value

    result = can_access_google_page(GOOGLE_URL)

    assert result == expected_result, (
        f"Failed with valid_google_url: {url_return_value}, "
        f"has_internet_connection: {conn_return_value}. "
        f"Expected: {expected_result}. Actual: {result}."
    )
