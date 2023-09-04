import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_accessible(
        self,
        mock_has_internet_connection: unittest.mock.Mock,
        mock_valid_google_url: unittest.mock.Mock
    ) -> None:
        url = "https://www.google.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_invalid_url(
        self,
        mock_has_internet_connection: unittest.mock.Mock,
        mock_valid_google_url: unittest.mock.Mock
    ) -> None:
        url = "https://www.invalidurl.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_google_page_no_internet(
        self,
        mock_has_internet_connection: unittest.mock.Mock,
        mock_valid_google_url: unittest.mock.Mock
    ) -> None:
        url = "https://www.google.com"
        result = can_access_google_page(url)
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
