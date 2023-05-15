import pytest

from unittest.mock import patch

from app.main import can_access_google_page

from typing import Callable


@pytest.fixture()
def mocked_google_url() -> Callable:
    with patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet_connection() -> Callable:
    with patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_if_everything_works(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://www.facebook.com/") == "Accessible"


def test_everything_does_not_work(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.faceboo.com/"
    ) == "Not accessible"


def test_if_url_is_not_valid(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page(
        "https://www.facebook.com/"
    ) == "Not accessible"


def test_if_no_internet_connection(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable
) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.faceboo.com/"
    ) == "Not accessible"
