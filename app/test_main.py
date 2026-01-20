from unittest import mock
from typing import Callable
from app.main import (
    can_access_google_page
)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_url_is_valid_and_connection_exists(
        mocked_url: Callable,
        mocked_connection: Callable
) -> None:

    example_url = "https://www.google.com"
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page(example_url) == "Accessible"

    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page(example_url) == "Not accessible"

    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page(example_url) == "Not accessible"

    mocked_connection.return_value = False
    mocked_url.return_value = False
    assert can_access_google_page(example_url) == "Not accessible"
