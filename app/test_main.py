import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_accessible(
            self,
            mock_has_internet_connection: any,
            mock_valid_google_url: any
    ) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Accessible")

        mock_valid_google_url.assert_called_once_with("https://www.google.com")
        mock_has_internet_connection.assert_called_once()

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_not_accessible_invalid_url(
            self,
            mock_has_internet_connection: any,
            mock_valid_google_url: any
    ) -> None:

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://invalid-url.com")

        self.assertEqual(result, "Not accessible")

        mock_valid_google_url.assert_called_once_with(
            "https://invalid-url.com"
        )

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_not_accessible_no_internet_connection(
            self,
            mock_has_internet_connection: any,
            mock_valid_google_url: any
    ) -> None:

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Accessible")

        mock_valid_google_url.assert_called_once_with("https://www.google.com")
        mock_has_internet_connection.assert_called_once()
