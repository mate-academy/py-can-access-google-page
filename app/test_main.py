import unittest
from unittest.mock import patch, Mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible(
            self,
            mock_has_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https//www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_no_internet(
            self,
            mock_has_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_invalid_url(
            self,
            mock_has_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_no_internet_and_invalid_url(
            self,
            mock_has_internet_connection: Mock,
            mock_valid_google_url: Mock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
