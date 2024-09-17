import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,url_is_valid,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Accessible - when has connection and url is valid",
        "Not accessible - when has connection and url is not valid",
        "Not accessible - when doesn't have connection and url is valid",
        "Not accessible - when doesn't have connection and url is not valid"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        has_internet_connection: mock,
        valid_google_url: mock,
        has_connection: bool,
        url_is_valid: bool,
        expected_result: str
) -> None:

    has_internet_connection.return_value = has_connection
    valid_google_url.return_value = url_is_valid

    assert can_access_google_page("https://google.com/") == expected_result
