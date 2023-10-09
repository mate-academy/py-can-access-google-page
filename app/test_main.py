from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "function_valid_google_url,"
    "function_has_internet_connection,"
    "expect_result", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_internet_connection(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool,
        function_valid_google_url: bool,
        function_has_internet_connection: bool,
        expect_result: bool
) -> None:
    mocked_valid_google_url.return_value = function_valid_google_url
    mocked_has_internet_connection.return_value = (
        function_has_internet_connection
    )
    result = can_access_google_page("https://www.google.com.ua/")
    assert result == expect_result
