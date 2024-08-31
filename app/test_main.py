import unittest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_accessible(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_due_to_no_internet(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_due_to_no_internet_and_invalid_url(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
