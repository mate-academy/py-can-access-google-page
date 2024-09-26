import pytest
from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "expected_valid_url,expected_connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mocked_url: Callable,
        mocked_connection: Callable,
        expected_valid_url: bool,
        expected_connection: bool,
        expected_result: str
) -> None:
    mocked_url.return_value = expected_valid_url
    mocked_connection.return_value = expected_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
