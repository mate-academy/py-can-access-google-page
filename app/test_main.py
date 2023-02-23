import unittest
from unittest.mock import patch
from datetime import datetime
from app.main import can_access_google_page


class TestCanAccessPage(unittest.TestCase):
    def test_valid_url_and_internet_connection(self) -> None:
        with patch("app.main.valid_google_url", return_value=True):
            with patch("app.main.has_internet_connection", return_value=True):
                url = "https://www.google.com/"
                result = can_access_google_page(url)
                self.assertEqual(result, "Accessible")

    def test_invalid_url_valid_internet_connection(self) -> None:
        with patch("app.main.valid_google_url", return_value=False):
            with patch("app.main.has_internet_connection", return_value=True):
                url = "https://www.Geag0Le.com/"
                result = can_access_google_page(url)
                self.assertEqual(result, "Not accessible")

    def test_out_of_hours(self) -> None:
        with patch("app.main.valid_google_url", return_value=True):
            with patch("app.main.has_internet_connection", return_value=False):
                current_time = datetime(2023, 2, 22, 23, 0, 0)
                with patch(
                        "app.main.datetime.datetime", return_value=current_time
                ):
                    url = "https://www.google.com/"
                    result = can_access_google_page(url)
                    self.assertEqual(result, "Not accessible")
