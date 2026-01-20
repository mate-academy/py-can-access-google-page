# app/test_main.py
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
    mocked_connection: mock.MagicMock, mocked_valid: mock.MagicMock
) -> None:
    mocked_valid.return_value = True
    mocked_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_but_no_connection(
    mocked_connection: mock.MagicMock, mocked_valid: mock.MagicMock
) -> None:
    mocked_valid.return_value = True
    mocked_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_even_with_connection(
    mocked_connection: mock.MagicMock, mocked_valid: mock.MagicMock
) -> None:
    mocked_valid.return_value = False
    mocked_connection.return_value = True
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_no_connection(
    mocked_connection: mock.MagicMock, mocked_valid: mock.MagicMock
) -> None:
    mocked_valid.return_value = False
    mocked_connection.return_value = False
    result = can_access_google_page("https://example.com")
    assert result == "Not accessible"
