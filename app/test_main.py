from app.main import can_access_google_page
from typing import Callable
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "url,has_connection,valid_url,expected_output",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://zweeqf.com", True, False, "Not accessible"),
        ("https://xcbvn.com", False, True, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_correct_output(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        url: str,
        valid_url: str,
        has_connection: bool,
        expected_output: str
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_output
