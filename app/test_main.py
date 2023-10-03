import pytest

from unittest import mock

from app.main import can_access_google_page

from typing import Callable


@pytest.mark.parametrize("connection_result, url_result, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible"),
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_connection: Callable,
        mocked_url: Callable,
        connection_result: bool,
        url_result: bool,
        expected_result: str
) -> None:
    mocked_connection.return_value = connection_result
    mocked_url.return_value = url_result

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == expected_result
