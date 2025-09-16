import pytest
from unittest.mock import patch
import sys
import os
from typing import Any

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


class TestCanAccessGooglePage:

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_valid_url_with_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = True
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_valid_url_without_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = False
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
        mock_internet.assert_called()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_invalid_url_with_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"
        mock_internet.assert_called()
        mock_valid_url.assert_called()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_invalid_url_without_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = False
        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"
        mock_internet.assert_called()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_empty_url(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page("")
        assert result == "Not accessible"
        mock_internet.assert_called()
        mock_valid_url.assert_called()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_none_url(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page(None)
        assert result == "Not accessible"
        mock_internet.assert_called()
        mock_valid_url.assert_called()

    @pytest.mark.parametrize("url", [
        "https://google.com",
        "https://www.google.com",
        "http://google.com",
        "https://google.co.uk",
        "https://www.google.ca"
    ])
    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_different_google_urls(
        self, mock_valid_url: Any, mock_internet: Any, url: str
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = True
        result = can_access_google_page(url)
        assert result == "Accessible"

    @pytest.mark.parametrize("url", [
        "not_a_url",
        "ftp://google.com",
        "https://",
        "google.com",
        "https://google",
        "   https://www.google.com   "
    ])
    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_malformed_urls(
        self, mock_valid_url: Any, mock_internet: Any, url: str
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page(url)
        assert result == "Not accessible"

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_only_connection_not_enough(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True
        result = can_access_google_page("https://example.com")
        assert result == "Not accessible"

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_only_valid_url_not_enough(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = False
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_both_conditions_needed(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = True
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
