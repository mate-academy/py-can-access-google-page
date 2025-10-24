from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_access_page_calls_necessary_functions(
        mocked_has_internet_connection: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        can_access_google_page("https://www.google.com/")
        mocked_has_internet_connection.assert_called_once()
        mocked_valid_url.assert_called_once_with("https://www.google.com/")


@mock.patch("app.main.has_internet_connection")
def test_page_access_with_valid_url_and_good_connection(
        mocked_has_internet_connection: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        mocked_has_internet_connection.return_value = True
        mocked_valid_url.return_value = True
        assert (can_access_google_page("") == "Accessible")


@mock.patch("app.main.has_internet_connection")
def test_page_access_with_invalid_url_and_bad_connection(
        mocked_has_internet_connection: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        mocked_has_internet_connection.return_value = False
        mocked_valid_url.return_value = False
        assert (can_access_google_page("") == "Not accessible")


@mock.patch("app.main.has_internet_connection")
def test_page_access_with_invalid_url_and_good_connection(
        mocked_has_internet_connection: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        mocked_has_internet_connection.return_value = True
        mocked_valid_url.return_value = False
        assert (can_access_google_page("") == "Not accessible")


@mock.patch("app.main.has_internet_connection")
def test_page_access_with_valid_url_and_bad_connection(
        mocked_has_internet_connection: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        mocked_has_internet_connection.return_value = False
        mocked_valid_url.return_value = True
        assert (can_access_google_page("") == "Not accessible")
