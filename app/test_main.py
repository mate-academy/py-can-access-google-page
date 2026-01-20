import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    def test_can_access_google_page_accessible(self) -> None:
        """Test when both internet and URL are valid."""
        url = "http://www.google.com"
        with patch("app.main.has_internet_connection", return_value=True), \
             patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page(url)
            self.assertEqual(result, "Accessible")

    def test_can_access_google_page_no_internet(self) -> None:
        """Test when there is no internet connection."""
        url = "http://www.google.com"
        with patch("app.main.has_internet_connection", return_value=False), \
             patch("app.main.valid_google_url", return_value=True):
            result = can_access_google_page(url)
            self.assertEqual(result, "Not accessible")

    def test_can_access_google_page_invalid_url(self) -> None:
        """Test when the URL is invalid."""
        url = "http://invalid.url"
        with patch("app.main.has_internet_connection", return_value=True), \
             patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page(url)
            self.assertEqual(result, "Not accessible")

    def test_can_access_google_page_no_internet_and_invalid_url(self) -> None:
        """Test when both internet and URL are invalid."""
        url = "http://invalid.url"
        with patch("app.main.has_internet_connection", return_value=False), \
             patch("app.main.valid_google_url", return_value=False):
            result = can_access_google_page(url)
            self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
