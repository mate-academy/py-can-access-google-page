import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_url_with_internet(
            self,
            mock_internet: unittest.mock.MagicMock,
            mock_valid_url: unittest.mock.MagicMock
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = True

        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_internet: unittest.mock.MagicMock,
            mock_valid_url: unittest.mock.MagicMock
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("https://www.fakegoogle.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_no_internet(
            self,
            mock_internet: unittest.mock.MagicMock,
            mock_valid_url: unittest.mock.MagicMock
    ) -> None:
        mock_valid_url.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_both_conditions(
            self,
            mock_internet: unittest.mock.MagicMock,
            mock_valid_url: unittest.mock.MagicMock
    ) -> None:
        mock_valid_url.return_value = False
        mock_internet.return_value = False

        result = can_access_google_page("https://www.fakegoogle.com")
        self.assertEqual(result, "Not accessible")
