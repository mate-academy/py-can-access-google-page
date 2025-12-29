import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_when_has_internet_and_valid_url(mock_valid_url, mock_internet):
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("http://www.google.com")
    assert result == "Accessible"

@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_when_no_internet(mock_valid_url, mock_internet):
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_when_invalid_url(mock_valid_url, mock_internet):
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_when_no_internet_and_invalid_url(mock_valid_url, mock_internet):
    mock_internet.return_value = False
    mock_valid_url.return_value = False

    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
