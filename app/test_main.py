import pytest
from unittest.mock import patch
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.dirname(current_dir))

try:
    from main import can_access_google_page
except ImportError:
    try:
        from app.main import can_access_google_page
    except ImportError:
        def can_access_google_page(url: str) -> str:
            return "Mock implementation"


def test_accessible_with_both_conditions() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_not_accessible_without_internet() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_not_accessible_with_invalid_url() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"


def test_not_accessible_without_both() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"


def test_empty_url_not_accessible() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("")
        assert result == "Not accessible"


def test_none_url_not_accessible() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page(None)
        assert result == "Not accessible"


def test_only_internet_should_fail() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://example.com")
        assert result != "Accessible"
        assert result == "Not accessible"


def test_only_valid_url_should_fail() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result != "Accessible"
        assert result == "Not accessible"


def test_or_logic_prevention() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://example.com")
        assert result == "Not accessible"


def test_must_check_both_functions() -> None:
    with patch("main.valid_google_url", return_value=True) as mock_url, \
         patch("main.has_internet_connection", return_value=True) as mock_conn:
        can_access_google_page("https://www.google.com")
        mock_url.assert_called()
        mock_conn.assert_called()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
