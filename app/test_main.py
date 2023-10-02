import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_page_accessible(self,
                             mock_has_internet_connection: str,
                             mock_valid_google_url: str) -> None:

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_page_not_accessible(self,
                                 mock_has_internet_connection: str,
                                 mock_valid_google_url: str) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_page_invalid_url(self,
                              mock_has_internet_connection: str,
                              mock_valid_google_url: str) -> None:

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False

        result = can_access_google_page("https://www.example.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
