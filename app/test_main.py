from app.main import can_access_google_page

from unittest import mock

from unittest.mock import MagicMock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_internet_valid_url(
        valid_google_url: MagicMock,
        has_internet_connection: MagicMock
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_internet_invalid_url(
        valid_google_url: MagicMock,
        has_internet_connection: MagicMock
) -> None:
    valid_google_url.return_value = False
    has_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet_valid_url(
        valid_google_url: MagicMock,
        has_internet_connection: MagicMock
) -> None:
    valid_google_url.return_value = True
    has_internet_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"
