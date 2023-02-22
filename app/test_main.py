from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url(
    mocked_valid_url: Callable, mocked_internet_connection: Callable
) -> bool:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet_connection(
    mocked_valid_url: Callable, mocked_internet_connection: Callable
) -> bool:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_are_internet_connection_valid_url(
    mocked_valid_url: Callable, mocked_internet_connection: Callable
) -> bool:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet_connection_not_valid_url(
    mocked_valid_url: Callable, mocked_internet_connection: Callable
) -> bool:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("www.google.com") == "Not accessible"
