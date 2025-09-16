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


def test_valid_url_with_internet_connection() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_valid_url_without_internet_connection() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_invalid_url_with_internet_connection() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"


def test_invalid_url_without_internet_connection() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"


def test_empty_url() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("")
        assert result == "Not accessible"


def test_none_url() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page(None)
        assert result == "Not accessible"


def test_connection_only_fails() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://example.com")
        assert result == "Not accessible"


def test_valid_url_only_fails() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_or_logic_fails_case_1() -> None:
    with patch("main.valid_google_url", return_value=True), \
         patch("main.has_internet_connection", return_value=False):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_or_logic_fails_case_2() -> None:
    with patch("main.valid_google_url", return_value=False), \
         patch("main.has_internet_connection", return_value=True):
        result = can_access_google_page("https://example.com")
        assert result == "Not accessible"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
