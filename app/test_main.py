from app.main import can_access_google_page
from unittest import mock
from typing import Any


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_return_accessible(
        mocked_internet_connection: Any,
        mocked_valid_google_url: Any
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("url") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_internet_connection_return_false(
        mocked_internet_connection: Any,
        mocked_valid_google_url: Any
) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_google_url.return_value = True
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_google_url_return_false(
        mocked_internet_connection: Any,
        mocked_valid_google_url: Any
) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("url") == "Not accessible"
