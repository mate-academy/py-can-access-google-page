import unittest
from unittest.mock import patch
from app.main import can_access_google_page

class TestCanAccessGooglePage(unittest.TestCase):

    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_can_access_google_page(self, mock_has_internet_connection, mock_valid_google_url):
        # Test when both valid_google_url and has_internet_connection return True
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page('http://www.google.com'), 'Accessible')

        # Test when only valid_google_url returns True
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page('http://www.google.com'), 'Not accessible')

        # Test when only has_internet_connection returns True
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page('http://www.google.com'), 'Not accessible')

        # Test when both valid_google_url and has_internet_connection return False
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page('http://www.google.com'), 'Not accessible')