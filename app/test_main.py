import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_cant_access_with_invalid_url(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool
    ) -> None:
        result = can_access_google_page("https://example.com")
        self.assertEqual(result, "Not accessible",
                         "Wrong url. Can not access the page")

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_cant_access_with_no_internet(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool
    ) -> None:
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible",
                         "No internet, check your connection")

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_cant_access_with_no_internet_and_invalid_url(
            self,
            mock_has_internet: bool,
            mock_valid_url: bool
    ) -> None:
        result = can_access_google_page("https://example.com")
        self.assertEqual(result, "Not accessible",
                         "No internet and wrong url")


if __name__ == "__main__":
    unittest.main()
