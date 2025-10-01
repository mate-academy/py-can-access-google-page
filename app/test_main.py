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
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=True)
    def test_not_accessible_when_no_internet(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_invalid_url(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        result = can_access_google_page("https://fake-url.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=False)
    def test_not_accessible_when_both_conditions_false(
        self,
        mock_valid: MagicMock,
        mock_internet: MagicMock,
    ) -> None:
        result = can_access_google_page("https://fake-url.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
