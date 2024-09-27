import unittest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_accessible_google_page(
            self, mock_has_internet_connection: bool,
            mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        result = can_access_google_page("https://invalid-url.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_no_internet(
            self,
            mock_has_internet_connection: bool,
            mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
