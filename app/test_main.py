import unittest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self, mock_internet, mock_valid_url):
        test_cases = [
            ("https://www.google.com", True, True, "Accessible"),
            ("https://www.google.com", True, False, "Not accessible"),
            ("https://www.fake-google.com", False, True, "Not accessible"),
            ("https://www.fake-google.com", False, False, "Not accessible"),
            ("", False, True, "Not accessible"),
            (None, False, True, "Not accessible"),
        ]

        for url, valid_url, internet_connection, expected in test_cases:
            mock_valid_url.return_value = valid_url
            mock_internet.return_value = internet_connection

            result = can_access_google_page(url)
            self.assertEqual(result, expected)



