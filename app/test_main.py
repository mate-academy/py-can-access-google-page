import unittest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_page(
            self,
            mock_has_internet_connection: MagicMock,
            mock_valid_google_url: MagicMock) -> None:

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://www.google.com/")

        expected = "Accessible"

        self.assertEqual(result, expected)

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_has_internet_connection: MagicMock,
            mock_valid_google_url: MagicMock) -> None:

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True

        result = can_access_google_page("https://invalid.google.com/")
        expected = "Not accessible"
        self.assertEqual(result, expected)

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_no_internet(
            self,
            mock_has_internet_connection: MagicMock,
            mock_valid_google_url: MagicMock) -> None:

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False

        result = can_access_google_page("https://www.google.com/")
        expected = "Not accessible"
        self.assertEqual(result, expected)

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_invalid_url_and_no_internet(
            self,
            mock_has_internet_connection: MagicMock,
            mock_valid_google_url: MagicMock) -> None:

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False

        result = can_access_google_page("https://invalid.google.com/")
        expected = "Not accessible"
        self.assertEqual(result, expected)
