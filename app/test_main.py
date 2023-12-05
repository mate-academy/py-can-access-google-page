from unittest import mock
from typing import Any
import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_url(request: Any) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = request.param
        yield mocked_url


@pytest.fixture
def mocked_internet_connection(request: Any) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        mocked_connection.return_value = request.param
        yield mocked_connection


@pytest.mark.parametrize("mocked_url, mocked_internet_connection, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible"),
])
def test_can_access_google_page(mocked_url, mocked_internet_connection, expected_result):
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
