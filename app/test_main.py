from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_has_connection(
        mocked_connection: Callable,
        mocked_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("test.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_has_connection(
        mocked_connection: Callable,
        mocked_url: Callable
) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("test.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
        mocked_connection: Callable,
        mocked_url: Callable
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("test.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_no_connection(
        mocked_connection: Callable,
        mocked_url: Callable
) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = False
    assert can_access_google_page("test.com") == "Not accessible"
