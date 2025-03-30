import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_if_all_true(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool,
    ) -> None:

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_if_invalid_url(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool,
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        result = can_access_google_page("https://invalidurl.com")

        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_if_false_internet_connection(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool,
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_if_all_false(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool,
    ) -> None:

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        result = can_access_google_page("https://invalidurl.com")

        self.assertEqual(result, "Not accessible")
