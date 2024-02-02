from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert (can_access_google_page("https://translate.google.com/?hl=uk")
            == "Accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert (can_access_google_page("translate.google.com/?hl=uk")
            == "Not accessible")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_url(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert (can_access_google_page("https://translate.google.com/?hl=uk")
            == "Not accessible")
