import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,is_valid_google_url,has_internet_connection,output",
    [
        (
            "https://www.google.com.ua/",
            True,
            True,
            "Accessible"
        ),
        (
            "https://www.google.com.ua/",
            True,
            False,
            "Not accessible"
        ),
        (
            "https://www.google.com.ua/",
            False,
            True,
            "Not accessible"
        ),
        (
            "https://www.google.com.ua/",
            False,
            False,
            "Not accessible"
        ),
    ],
    ids=[
        "Google url is valid, has internet connection",
        "Google url is valid, has not internet connection",
        "Google url is not valid, has internet connection",
        "Google url is not valid, has not internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        url: str,
        is_valid_google_url: bool,
        has_internet_connection: bool,
        output: str
) -> None:
    mocked_valid_google_url.return_value = is_valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page(url) == output
