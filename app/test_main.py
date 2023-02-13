from unittest import mock
from typing import Any

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_only_connection_false(
    mocked_url: Any,
    mocked_connection: Any
) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_only_url_false(
    mocked_url: Any,
    mocked_connection: Any
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_and_connection_false(
    mocked_url: Any,
    mocked_connection: Any
) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"
