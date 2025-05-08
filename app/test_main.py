from unittest.mock import patch
from app.main import can_access_google_page
import pytest

def test_accessible_for_valid_url_and_internet():
    with patch("app.main.valid_google_url", return_value=True), \
        patch("app.main.has_internet_connection", return_value=True):

        result = can_access_google_page("https://google.com")
        assert result == "Accessible"

def test_accessible_for_bad_url_and_internet():
    with patch("app.main.valid_google_url", return_value=False), \
        patch("app.main.has_internet_connection", return_value=False):

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"


def test_accessible_for_bad_url():
    with patch("app.main.valid_google_url", return_value=True), \
        patch("app.main.has_internet_connection", return_value=False):

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"

def test_accessible_for_bad_internet():
    with patch("app.main.valid_google_url", return_value=False), \
        patch("app.main.has_internet_connection", return_value=True):

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"