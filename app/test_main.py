import unittest
from unittest.mock import patch
from app.main import can_access_google_page
from collections.abc import Callable


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_valid_url_and_connection_exists(self,
                                             mock_internet_connection: Callable,
                                             mock_valid_url: Callable) -> None:
        mock_internet_connection.return_value = True
        mock_valid_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"),
                         "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_valid_url_but_no_connection(self,
                                         mock_internet_connection: Callable,
                                         mock_valid_url: Callable) -> None:
        mock_internet_connection.return_value = False
        mock_valid_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"),
                         "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_invalid_url_with_connection(self,
                                         mock_internet_connection: Callable,
                                         mock_valid_url: Callable) -> None:
        mock_internet_connection.return_value = True
        mock_valid_url.return_value = False
        self.assertEqual(can_access_google_page("https://www.invalidurl.com"),
                         "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_invalid_url_and_no_connection(self,
                                           mock_internet_connection: Callable,
                                           mock_valid_url: Callable) -> None:
        mock_internet_connection.return_value = False
        mock_valid_url.return_value = False
        self.assertEqual(can_access_google_page("https://www.invalidurl.com"),
                         "Not accessible")
