import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestGooglePageAccess(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_has_internet_connection: callable,
                                    mock_valid_google_url: callable) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"),
                         "Accessible")

        mock_valid_google_url.return_value = False
        self.assertEqual(can_access_google_page("https://www.notgoogle.com"),
                         "Not accessible")

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"),
                         "Not accessible")

        mock_valid_google_url.return_value = False
        self.assertEqual(can_access_google_page("https://www.notgoogle.com"),
                         "Not accessible")
