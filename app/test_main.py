from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_validation_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_func_1:
        yield mock_func_1


@pytest.fixture
def mocked_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_func_2:
        yield mock_func_2


def test_url_valid_connection_exists(
        mocked_validation_url: bool,
        mocked_connection: bool) -> None:
    mocked_validation_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://google.com.ua/") == "Accessible"


def test_url_invalid_connection_exists(
        mocked_validation_url: bool,
        mocked_connection: bool) -> None:
    mocked_validation_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("https://google.com.ua/") == "Not accessible"


def test_url_true_connection_lost(
        mocked_validation_url: bool,
        mocked_connection: bool) -> None:
    mocked_validation_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("https://google.com.ua/") == "Not accessible"


def test_url_invalid_connection_lost(
        mocked_validation_url: bool,
        mocked_connection: bool) -> None:
    mocked_validation_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("https://google.com.ua/") == "Not accessible"
