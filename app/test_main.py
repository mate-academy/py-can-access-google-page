import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url_validation:
        yield mocked_url_validation


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_valid_url_with_no_connection(
        mocked_valid_google_url: None,
        mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("httt//xyz.com") == "Not accessible"


def test_invalid_url_with_connection(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("httt//xyz@@@com") == "Not accessible"


def test_invalid_url_with_no_connection(
        mocked_valid_google_url: None,
        mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("httt//xyz@@.com") == "Not accessible"


def test_valid_url_with_connection(
        mocked_valid_google_url: None,
        mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("httt//xyz.com") == "Accessible"
