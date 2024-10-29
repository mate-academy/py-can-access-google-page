import pytest
from unittest.mock import patch
from typing import Callable
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "expected_url_address, expected_web_connection, expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="Have an Internet connection and a valid URL-address"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="URL-address is valid, but "
               "there is no connection to the Internet"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="There is a connection to the "
               "Internet, but the address is not valid"
        )
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: Callable,
        mocked_web_connection: Callable,
        expected_url_address: bool,
        expected_web_connection: bool,
        expected_result: str
) -> None:
    mocked_url.return_value = expected_url_address
    mocked_web_connection.return_value = expected_web_connection
    assert can_access_google_page("https://www.google.com") == expected_result
