import unittest
from typing import Any
from unittest import mock, TestCase
from unittest.mock import patch

from app.main import (valid_google_url,
                      has_internet_connection,
                      can_access_google_page)


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=True)
    def test_accessible_when_internet_and_valid_url(
            self,
            has_internet_connection: bool,
            valid_google_url: bool
    ) -> None:
        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=True)
    def test_not_accessible_when_no_internet(
            self,
            has_internet_connection: bool,
            valid_google_url: bool
    ) -> None:
        result = can_access_google_page("http://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_invalid_url(
            self,
            has_internet_connection: bool,
            valid_google_url: bool
    ) -> None:
        result = can_access_google_page("http://invalid-url.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_no_internet_and_invalid_url(
            self,
            has_internet_connection: bool,
            valid_google_url: bool
    ) -> None:
        result = can_access_google_page("http://invalid-url.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()


class TestValidGoogleURL(TestCase):

    @mock.patch("requests.get")
    def test_valid_google_url(self, mock_get: Any) -> None:

        mock_get.return_value.status_code = 200

        result = valid_google_url("https://www.google.com")
        self.assertTrue(result)

        mock_get.return_value.status_code = 404
        result = valid_google_url("https://www.google.com/nonexistentpage")
        self.assertFalse(result)


class TestHasInternetConnection(TestCase):

    @mock.patch("datetime.datetime")
    def test_has_internet_connection(self, mock_datetime: Any) -> None:
        mock_datetime.now.return_value.hour = 8

        result = has_internet_connection()
        self.assertTrue(result)

        mock_datetime.now.return_value.hour = 4

        result = has_internet_connection()
        self.assertFalse(result)
