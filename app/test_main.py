from unittest import mock
from app.main import can_access_google_page
from typing import Callable


Google_home = "www.google.com"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(Google_home) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(Google_home) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_url_no_internet(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(Google_home) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_url_internet(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(Google_home) == "Accessible"
