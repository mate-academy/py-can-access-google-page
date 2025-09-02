import pytest
from unittest.mock import patch
from app.main import can_access_google_page

def test_accessible_when_both_true():
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("http://google.com")
        assert result == "Accessible"

def test_not_accessible_when_only_connection():
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"

def test_not_accessible_when_only_valid_url():
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"

def test_not_accessible_when_both_false():
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"
