from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_no_valid_url_and_connection_does_not_exist(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_if_no_valid_google_url(
        mocked_has_internet_connection: Callable
) -> None:
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page(
        "https://httpstat.us/404"
    ) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_if_no_internet_connection(
        mocked_has_internet_connection: Callable
) -> None:
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_has_internet_connection: Callable
) -> None:
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"
