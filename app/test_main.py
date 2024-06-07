import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_accessible_google_page(
            self,
            mock_valid_url: str,
            mock_internet_connection: str
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_invalid_url(
            self,
            mock_valid_url: str,
            mock_internet_connection: str
    ) -> None:
        result = can_access_google_page("https://invalid-url.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_no_internet_connection(
            self,
            mock_valid_url: str,
            mock_internet_connection: str
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
