from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert (can_access_google_page("https://www.google.com.ua/")
            == "Accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_google_page(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = False
    assert (can_access_google_page("https://www.google.com.ua/")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_internet_connection_false(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = False
    assert (can_access_google_page("https://www.google.com.ua/")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_url_false(
        mocked_google_url: Callable,
        mocked_internet_connection: Callable) -> None:
    mocked_google_url.return_value = False
    mocked_internet_connection.return_value = True
    assert (can_access_google_page("https://www.google.com.ua/")
            == "Not accessible")
