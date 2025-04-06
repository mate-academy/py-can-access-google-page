import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_with_internet_and_valid_url(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool,) -> None:

        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        result = can_access_google_page("http://google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_without_internet(self, mock_has_internet: bool,
                                             mock_valid_url: bool) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True

        result = can_access_google_page("http://google.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_with_invalid_url(self, mock_has_internet: bool,
                                             mock_valid_url: bool) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False

        result = can_access_google_page("http://invalid-url.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
