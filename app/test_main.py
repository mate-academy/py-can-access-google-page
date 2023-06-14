from unittest import mock

from app.main import can_access_google_page

from typing import Callable


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_with_connection_and_valid_url(
        mocked_connection: Callable,
        mocked_valid_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page("url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_without_connection(
        mocked_connection: Callable,
        mocked_valid_url: Callable
) -> None:
    mocked_connection.return_value = False
    mocked_valid_url.return_value = True

    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_with_invalid_url(
        mocked_connection: Callable,
        mocked_valid_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_valid_url.return_value = False

    assert can_access_google_page("url") == "Not accessible"
