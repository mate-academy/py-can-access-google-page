import unittest
from unittest.mock import patch
from typing import Any
import requests
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    @patch("app.main.requests.get")
    def test_accessible_google_page(self, mock_get: Any,
                                    mock_has_internet_connection: bool,
                                    mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        mock_get.return_value.status_code = 200

        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    @patch("app.main.requests.get")
    def test_not_accessible_invalid_url(self, mock_get: Any,
                                        mock_has_internet_connection: bool,
                                        mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("http://www.invalid-google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    @patch("app.main.requests.get")
    def test_not_accessible_no_internet(self,
                                        mock_get: Any,
                                        mock_has_internet_connection: bool,
                                        mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False

        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    @patch("app.main.requests.get")
    def test_not_accessible_request_exception(self,
                                              mock_get: Any,
                                              mock_has_internet_connection:
                                              bool, mock_valid_google_url:
                                              bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        mock_get.side_effect = requests.RequestException

        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Accessible")


if __name__ == "__main__":
    unittest.main()
