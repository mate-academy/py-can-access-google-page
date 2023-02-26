import unittest
from unittest.mock import patch
from datetime import datetime
from app.main import can_access_google_page


class TestCanAccessPage(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "https://www.google.com/"
        self.invalid_url = "https://www.Geag0Le.com/"
        self.current_time = datetime(2023, 2, 22, 23, 0, 0)

    def test_valid_url_and_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=True),
            patch("app.main.has_internet_connection", return_value=True)
        ):
            result = can_access_google_page(self.url)
            self.assertEqual(result, "Accessible",
                             f"Expected 'Accessible' but got '{result}'.")

    def test_invalid_url_valid_internet_connection(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=False),
            patch("app.main.has_internet_connection", return_value=True)
        ):
            result = can_access_google_page(self.invalid_url)
            self.assertEqual(result, "Not accessible",
                             f"Expected 'Not accessible' but got '{result}'.")

    def test_out_of_hours(self) -> None:
        with (
            patch("app.main.valid_google_url", return_value=True),
            patch("app.main.has_internet_connection", return_value=False),
            patch("app.main.datetime.datetime", return_value=self.current_time)
        ):
            result = can_access_google_page(self.url)
            self.assertEqual(result, "Not accessible",
                             f"Expected 'Not accessible' but got '{result}'.")
