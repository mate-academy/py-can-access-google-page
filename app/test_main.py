from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page

url = "http://www.google.com"


@pytest.fixture()
def mocked_valid_google_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_has_internet_connection() -> Callable:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "valid_url,connection,result", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_should_return_correct_string(
        valid_url: bool,
        connection: bool,
        result: str,
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page(url) == result
