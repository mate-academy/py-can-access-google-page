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
        mock_valid_url.assert_called_once_with("https://www.google.com")
        mock_internet.assert_called_once()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_valid_url_without_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
        mock_internet.assert_called_once()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_invalid_url_with_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:

        mock_valid_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("https://www.example.com")
        assert result == "Not accessible"
        mock_valid_url.assert_called_once_with("https://www.example.com")
        mock_internet.assert_called_once()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_invalid_url_without_internet_connection(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:

        mock_valid_url.return_value = False
        mock_internet.return_value = False

        result = can_access_google_page("https://www.example.com")

        assert result == "Not accessible"

        mock_internet.assert_called_once()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_empty_url(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:

        mock_valid_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("")

        assert result == "Not accessible"
        mock_valid_url.assert_called_once_with("")
        mock_internet.assert_called_once()

    @patch("main.has_internet_connection")
    @patch("main.valid_google_url")
    def test_none_url(
        self, mock_valid_url: Any, mock_internet: Any
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page(None)

        assert result == "Not accessible"
        mock_valid_url.assert_called_once_with(None)
        mock_internet.assert_called_once()

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
