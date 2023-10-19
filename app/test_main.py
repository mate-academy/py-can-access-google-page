import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_valid_url_and_interned_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_invalid_url_and_interned_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google/") == "Not accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_valid_url_and_no_interned_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"

@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_with_invalid_url_and_no_interned_connection(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google/") == "Not accessible"
