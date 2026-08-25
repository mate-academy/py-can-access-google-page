from unittest import mock
from typing import Any
import pytest

import app.main
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected",
                         [(True, True, "Accessible")])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_internet_connection: Any,
        mocked_valid_url: Any,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    mocked_internet_connection.return_value = has_connection
    mocked_valid_url.return_value = valid_url

    result = app.main.can_access_google_page("http://google.com")

    assert result == expected


@pytest.mark.parametrize("valid_url, has_connection, expected",
                         [(True, False, "Not accessible")])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
        mocked_internet_connection: Any,
        mocked_valid_url: Any,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    mocked_internet_connection.return_value = has_connection
    mocked_valid_url.return_value = has_connection

    result = app.main.can_access_google_page("http://google.com")

    assert result == expected


@pytest.mark.parametrize("valid_url, has_connection, expected",
                         [(False, True, "Not accessible")])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exists(
        mocked_internet_connection: Any,
        mocked_valid_url: Any,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    mocked_internet_connection.return_value = has_connection
    mocked_valid_url.return_value = valid_url
    result = app.main.can_access_google_page("http://google.com")

    assert result == expected


@pytest.mark.parametrize("valid_url, has_connection, expected",
                         [(False, False, "Not accessible")])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_no_connection(
        mocked_internet_connection: Any,
        mocked_valid_url: Any,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    mocked_internet_connection.return_value = has_connection
    mocked_valid_url.return_value = valid_url
    result = app.main.can_access_google_page("http://google.com")

    assert result == expected


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_can_access_google_page_is_called(
        mocked_internet_access: Any,
        mocked_valid_url: Any
) -> None:
    can_access_google_page(url="https://www.google.com")
    mocked_internet_access.assert_called_once()
    mocked_valid_url.assert_called()
