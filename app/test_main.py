import unittest
from unittest.mock import patch
from datetime import datetime
from typing import Any
from app.main import valid_google_url, \
    has_internet_connection, \
    can_access_google_page


class TestGoogleFunctions(unittest.TestCase):

    @patch("requests.get")
    def test_valid_google_url(self, mock_get: Any) -> None:
        mock_get.return_value.status_code = 200
        self.assertTrue(valid_google_url("https://www.google.com"))
        mock_get.return_value.status_code = 404
        self.assertFalse(valid_google_url("https://www.invalid.com"))

    def test_has_internet_connection(self) -> None:
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 25, 8, 0, 0)
            self.assertTrue(has_internet_connection())
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 25, 2, 0, 0)
            self.assertFalse(has_internet_connection())

    @patch("requests.get")
    def test_can_access_google_page(self, mock_get: Any) -> None:
        mock_get.return_value.status_code = 200
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 25, 8, 0, 0)
            self.assertEqual(can_access_google_page(
                "https://www.google.com"), "Accessible")
        mock_get.return_value.status_code = 404
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 25, 8, 0, 0)
            self.assertEqual(can_access_google_page(
                "https://www.invalid.com"), "Not accessible")


if __name__ == "__main__":
    unittest.main()
