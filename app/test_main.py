from unittest import mock
from typing import Any


import pytest


from app.main import can_access_google_page


link = "https://google.com"


@pytest.fixture()
def mocked_valid_google_url() -> Any:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> Any:
    with (mock.patch("app.main.has_internet_connection")
          as mock_internet_connection):
        yield mock_internet_connection


def test_access_google_page_calls_functions(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any
) -> None:
    can_access_google_page(link)
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(link)


def test_access_google_page_no_internet_connection(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any
) -> None:
    mocked_has_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page(link) == "Not accessible"


def test_access_google_page_invalid_google_url(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page(link) == "Not accessible"


def test_access_google_page_when_accessible(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("") == "Accessible"
