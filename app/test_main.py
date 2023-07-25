from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,has_connection,message",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Accessible google page if url is valid and has internet connection",
        "Not accessible google page if url isn`t valid while "
        "has internet connection",
        "Not accessible google page if url is valid but "
        "hasn't internet connection",
        "Not accessible google page if url isn`t valid and "
        "hasn't internet connection",
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        valid_google_url: mock,
        has_internet_connection: mock,
        is_valid: bool,
        has_connection: bool,
        message: str
) -> None:
    valid_google_url.return_value = is_valid
    has_internet_connection.return_value = has_connection
    url = "https://www.google.com/"

    assert can_access_google_page(url) == message
