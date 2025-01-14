import pytest
from app.main import has_internet_connection, valid_google_url, can_access_google_page

def test_has_internet_connection():
    assert isinstance(has_internet_connection(), bool), "Expected a boolean value"

def test_valid_google_url():
    assert valid_google_url("https://www.google.com") is True, "Valid URL should return True"
    assert valid_google_url("http://example.com") is False, "Invalid URL should return False"

def test_can_access_google_page():
    assert can_access_google_page("https://www.google.com") == "Accessible", "Should be accessible"
    assert can_access_google_page("http://example.com") == "Not accessible", "Should not be accessible"