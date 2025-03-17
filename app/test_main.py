import unittest
from unittest.mock import patch, Mock
import random
import datetime
from app.main import can_access_google_page, valid_google_url, has_internet_connection


class TestUrlAccess(unittest.TestCase):
    @patch("requests.get")
    @patch("datetime.datetime.now")
    @patch("app.main.valid_google_url", "app.main.has_internet_connection")
    def test_valid_url_and_connection_time(self, mock_internet: any,
                                           mock_url: any,
                                           mock_get: any,
                                           mock_time: any) -> None:

        mock_time.now.return_value = datetime.datetime(2024, 1, 1, random.randint(6, 23))

        mock_url.return_value = True
        mock_internet.return_value = True

        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = can_access_google_page(mock_url(), mock_internet())

        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
