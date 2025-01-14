import pytest
from unittest.mock import patch
from app.main import can_access_google_page, valid_google_url

def test_valid_google_url():
    assert valid_google_url("https://www.google.com") is True, "Valid Google URL should return True"
    assert valid_google_url("http://example.com") is False, "Invalid URL should return False"

@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://www.google.com") == "Accessible", "Should be accessible"

@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_cannot_access_if_only_valid_url(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("https://www.google.com") == "Not accessible", "Should not be accessible if no internet"

@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_cannot_access_if_only_connection(mock_valid_google_url, mock_has_internet_connection):
    assert can_access_google_page("http://example.com") == "Not accessible", "Should not be accessible if URL is invalid"
