import unittest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_accessible(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock) -> None:

        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True

        result = can_access_google_page("http://www.google.com")

        self.assertEqual(result, "Accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible(
            self,
            mock_valid_google_url: MagicMock,
            mock_has_internet_connection: MagicMock) -> None:

        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True

        result = can_access_google_page("http://www.google.com")

        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
