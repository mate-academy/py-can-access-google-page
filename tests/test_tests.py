import pytest
from unittest.mock import patch
from app.main import can_access_google_page

def test_cannot_access_if_only_connection():
    """Should return 'Not accessible' if internet exists but URL is invalid."""
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("https://invalid-url.com") == "Not accessible"


def test_cannot_access_if_only_valid_url():
    """Should return 'Not accessible' if URL is valid but no internet connection."""
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_if_both_valid():
    """Should return 'Accessible' only if both internet and valid URL exist."""
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert can_access_google_page("https://www.google.com") == "Accessible"


def test_cannot_access_if_both_invalid():
    """Should return 'Not accessible' if both internet and valid URL are missing."""
    with patch("app.main.has_internet_connection", return_value=False), \
         patch("app.main.valid_google_url", return_value=False):
        assert can_access_google_page("https://invalid-url.com") == "Not accessible"
