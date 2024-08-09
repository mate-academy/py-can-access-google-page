import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> bool:
    with mock.patch("app.main.valid_google_url") as mock_test_valid_google_url:
        yield mock_test_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> bool:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        yield mock_has_internet_connection


def test_can_access_page_when_url_and_connection_are_true(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("url") == "Accessible"


def test_cannot_access_page_when_google_url_is_false(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("url") == "Not accessible"


def test_cannot_access_page_when_connection_is_false(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
