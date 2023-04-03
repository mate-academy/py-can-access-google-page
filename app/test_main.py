from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_should_return_accessible_when_url_is_valid_and_has_connection(
    mocked_valid_google_url: mock, mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert (
        can_access_google_page(url="https://www.google.com/") == "Accessible"
    )


def test_should_return_not_accessible_when_url_is_valid_but_has_not_connection(
    mocked_valid_google_url: mock, mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert (
        can_access_google_page(url="https://www.google.com/")
        == "Not accessible"
    )


def test_should_return_not_accessible_when_url_is_not_valid_and_no_connection(
    mocked_valid_google_url: mock, mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert (
        can_access_google_page(url="https://www.google.com/")
        == "Not accessible"
    )


def test_should_return_not_accessible_when_url_is_not_valid_but_has_connection(
    mocked_valid_google_url: mock, mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert (
        can_access_google_page(url="https://www.google.com/")
        == "Not accessible"
    )
