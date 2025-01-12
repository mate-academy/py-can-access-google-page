import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_valid_url_and_internet_available(self, mock_int, mock_url):
        mock_url.return_value = True
        mock_int.return_value = True
        self.assertEqual(
            can_access_google_page("http://google.com"),
            "Accessible"
        )

    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_valid_url_and_internet_not_available(self, mock_int, mock_url):
        mock_url.return_value = True
        mock_int.return_value = False
        self.assertEqual(
            can_access_google_page("http://google.com"),
            "Not accessible"
        )

    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_invalid_url_and_internet_available(self, mock_int, mock_url):
        mock_url.return_value = False
        mock_int.return_value = True
        self.assertEqual(
            can_access_google_page("http://invalid.com"),
            "Not accessible"
        )

    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_invalid_url_and_internet_not_available(self, mock_int, mock_url):
        mock_url.return_value = False
        mock_int.return_value = False
        self.assertEqual(
            can_access_google_page("http://invalid.com"),
            "Not accessible"
        )

    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_edge_case_exception_handling(self, mock_int, mock_url):
        mock_url.side_effect = Exception("URL validation error")
        mock_int.return_value = True
        self.assertEqual(
            can_access_google_page("http://error.com"),
            "Not accessible"
        )


if __name__ == "__main__":
    unittest.main()
