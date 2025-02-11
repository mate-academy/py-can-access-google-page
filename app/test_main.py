import unittest
from unittest.mock import patch

from app.main import can_access_google_page



class TestCanAccessGooglePage(unittest.TestCase):
    
    @patch("main.valid_google_url")
    @patch("main.has_internet_connection")
    def test_accessible(self, mock_has_internet, mock_valid_url):
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"), "Accessible")
    
    @patch("main.valid_google_url")
    @patch("main.has_internet_connection")
    def test_no_internet(self, mock_has_internet, mock_valid_url):
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        self.assertEqual(can_access_google_page("https://www.google.com"), "Not accessible")
    
    @patch("main.valid_google_url")
    @patch("main.has_internet_connection")
    def test_invalid_url(self, mock_has_internet, mock_valid_url):
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        self.assertEqual(can_access_google_page("https://invalid-url.com"), "Not accessible")
    
    @patch("main.valid_google_url")
    @patch("main.has_internet_connection")
    def test_no_internet_and_invalid_url(self, mock_has_internet, mock_valid_url):
        mock_has_internet.return_value = False
        mock_valid_url.return_value = False
        self.assertEqual(can_access_google_page("https://invalid-url.com"), "Not accessible")


if __name__ == "__main__":
    unittest.main()