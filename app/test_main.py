from unittest import mock


import pytest


from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_should_get_google_page(
        mocked_has_internet_connection: bool,
        mocked_valid_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_should_not_get_google_page_if_no_connection(
        mocked_has_internet_connection: bool,
        mocked_valid_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com/")\
           == "Not accessible"


def test_should_not_get_google_page_if_no_page(
        mocked_has_internet_connection: bool,
        mocked_valid_google_url: bool
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("https://www.google.com/")\
           == "Not accessible"
