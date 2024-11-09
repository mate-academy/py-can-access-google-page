from unittest import mock
import pytest
from app.main import can_access_google_page  # Adjust the import based on your project structure


def test_can_access_google_page_accessible():
    # Mock valid_google_url to return True, indicating URL is valid
    with mock.patch("app.main.valid_google_url", return_value=True):
        # Mock has_internet_connection to return True, indicating internet is available
        with mock.patch("app.main.has_internet_connection", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"


def test_can_access_google_page_not_accessible_due_to_invalid_url():
    # Mock valid_google_url to return False, indicating URL is invalid
    with mock.patch("app.main.valid_google_url", return_value=False):
        # Mock has_internet_connection to return True, indicating internet is available
        with mock.patch("app.main.has_internet_connection", return_value=True):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_no_internet():
    # Mock valid_google_url to return True, indicating URL is valid
    with mock.patch("app.main.valid_google_url", return_value=True):
        # Mock has_internet_connection to return False, indicating no internet
        with mock.patch("app.main.has_internet_connection", return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"


def test_can_access_google_page_not_accessible_due_to_both_conditions():
    # Mock valid_google_url to return False, indicating URL is invalid
    with mock.patch("app.main.valid_google_url", return_value=False):
        # Mock has_internet_connection to return False, indicating no internet
        with mock.patch("app.main.has_internet_connection", return_value=False):
            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
