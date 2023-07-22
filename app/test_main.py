from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_valid_url_available_internet(mocked_internet_connection: Any) -> None:
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
def test_valid_url_unavailable_internet(
        mocked_internet_connection: Any
) -> None:
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_link_available_internet(
        mocked_valid_url: Any,
        mocked_internet_connection: Any
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = False
    assert can_access_google_page("https/google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_link_unavailable_internet(
        mocked_valid_url: Any,
        mocked_internet_connection: Any
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("https/google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
def test_if_the_valid_google_url_called(mocked_valid_url: Any) -> None:
    can_access_google_page("https://google.com")
    mocked_valid_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_if_the_has_internet_connection_called(
        mocked_internte_connection: Any
) -> None:
    can_access_google_page("https://google.com")
    mocked_internte_connection.assert_called_once()
