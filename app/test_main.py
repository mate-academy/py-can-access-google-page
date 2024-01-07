import unittest
from unittest.mock import patch, Mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_accessible(
            self, mock_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_not_accessible_invalid_url(
            self, mock_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        result = can_access_google_page("invalid_url")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_google_page_not_accessible_no_internet_connection(
            self, mock_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
