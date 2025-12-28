import pytest
from typing import Callable
from unittest import mock

from app.main import can_access_google_page


URL = "https://httpstat.us/404"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "is_has_connection,is_valid,result",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "no_valid_url_and_connection_does_not_exist",
        "no_valid_url_should_return_false",
        "no_internet_connection_should_return_false",
        "valid_url_and_connection_exists",
    ]
)
def test_can_access_page(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        is_has_connection: bool,
        is_valid: bool,
        result: str
) -> None:
    mocked_has_internet_connection.return_value = is_has_connection
    mocked_valid_google_url.return_value = is_valid

    assert can_access_google_page(URL) == result
