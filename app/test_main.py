from unittest import mock
from typing import Callable
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_correct_access(mocked_has_internet_connection: Callable,
                        mocked_valid_google_url: Callable) -> None:

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("some_url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_incorrect_access_has_not_internet_connection(
        mocked_has_internet_connection: Callable,
        mocked_valid_google_url: Callable) -> None:

    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_incorrect_access_invalid_google_url(
        mocked_has_internet_connection: Callable,
        mocked_valid_google_url: Callable) -> None:

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_incorrect_access_no_internet_invalid_url(
        mocked_has_internet_connection: Callable,
        mocked_valid_google_url: Callable) -> None:

    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("some_url") == "Not accessible"
