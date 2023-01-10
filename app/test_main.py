from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mocked_has_internet_connection:
        yield mocked_has_internet_connection


def test_can_access_google_page_if_url_false(
        mocked_valid_google_url: object,
        mocked_has_internet_connection: object
) -> None:
    test_url = "https://test_url"
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"


def test_can_access_google_page_if_url_false_connection_true(
        mocked_valid_google_url: object,
        mocked_has_internet_connection: object
) -> None:
    test_url = "https://test_url"
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Not accessible"


def test_can_access_google_page_if_url_true(
        mocked_valid_google_url: object,
        mocked_has_internet_connection: object
) -> None:
    test_url = "https://test_url"
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(test_url) == "Not accessible"


def test_can_access_google_page_if_url_true_and_connection_true(
        mocked_valid_google_url: object,
        mocked_has_internet_connection: object
) -> None:
    test_url = "https://test_url"
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(test_url) == "Accessible"
