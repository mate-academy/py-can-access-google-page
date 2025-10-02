import unittest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=True)
    def test_accessible_when_both_conditions_true(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        url = "https://www.google.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Accessible")
        mock_valid.assert_called_once_with(url)
        mock_internet.assert_called_once_with()

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=True)
    def test_not_accessible_when_no_internet(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        url = "https://www.google.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Not accessible")
        mock_valid.assert_called_once_with(url)
        mock_internet.assert_called_once_with()

    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_invalid_url(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        url = "https://fake-url.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Not accessible")
        mock_valid.assert_called_once_with(url)
        mock_internet.assert_called_once_with()

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_both_conditions_false(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        url = "https://fake-url.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Not accessible")
        mock_valid.assert_called_once_with(url)
        mock_internet.assert_called_once_with()
