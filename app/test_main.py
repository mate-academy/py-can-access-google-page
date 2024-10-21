import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestAccess(unittest.TestCase):
    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_valid_url_has_connection(
            self,
            mock_valid_google_url: bool,
            mock_has_internet_connection: bool
    ) -> None:

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Accessible"
        )

    @patch("app.main.valid_google_url")
    def test_invalid_url(
            self,
            mock_valid_google_url: bool
    ) -> None:

        mock_valid_google_url.return_value = False
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Not accessible"
        )

    @patch("app.main.has_internet_connection")
    def test_not_internet_connection(
            self,
            mock_has_internet_connection: bool
    ) -> None:

        mock_has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page(
            "https://www.google.com"), "Not accessible"
        )

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_invalid__url_not_connection(
            self,
            mock_valid_google_url: bool,
            mock_has_internet_connection: bool
    ) -> None:

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page(
            "https://www.google.com"), "Not accessible"
        )
