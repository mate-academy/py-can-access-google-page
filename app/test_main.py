from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        yield mocked_internet


def test_can_access_google_page_not_valid_url(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("wwww.google.com") == "Not accessible"


def test_can_access_google_page_no_internet_connection(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("wwww.google.com") == "Not accessible"


def test_can_access_google_page_no_internet_connection_not_valid_url(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("wwww.google.com") == "Not accessible"


def test_can_access_google_page_has_internet_connection_valid_url(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("wwww.google.com") == "Accessible"
