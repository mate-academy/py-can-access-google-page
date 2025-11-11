# app/test_main.py

from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_url_valid_and_internet_available(
    mock_internet: object, mock_valid_url: object
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid(
    mock_internet: object, mock_valid_url: object
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    result = can_access_google_page("https://invalid.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_internet: object, mock_valid_url: object
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_both_invalid(
    mock_internet: object, mock_valid_url: object
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    result = can_access_google_page("https://invalid.com")
    assert result == "Not accessible"
