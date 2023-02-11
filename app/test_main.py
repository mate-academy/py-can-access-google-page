import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as url_validation:
        yield url_validation


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as internet_connection:
        yield internet_connection


def test_valid_url_and_connection_exists(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert (
        can_access_google_page("https://www.google.com/maps") == "Accessible"
    ), "You can access page " \
       "if 'connection' and 'valid url' is True."


def test_valid_url_but_without_connection(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page(
            "https://www.google.com/maps"
        ) == "Not accessible"
    ), "You cannot access the page " \
       "if 'connection' is False and 'valid url' is True."


def test_invalid_url_and_without_connection(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert (
        can_access_google_page(
            "https:///www.google.com/maps"
        ) == "Not accessible"
    ), "You cannot access the page " \
       "if both 'connection' and 'valid url' are False."


def test_invalid_url_but_connection_exists(
        mocked_valid_google_url: callable,
        mocked_has_internet_connection: callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert (
        can_access_google_page(
            "https:///www.google.com/maps"
        ) == "Not accessible"
    ), "You cannot access the page " \
       "if 'connection' is True and 'valid url' is False."
