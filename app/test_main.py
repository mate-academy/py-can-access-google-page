import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible(
        self,
        mock_has_internet: unittest.mock.Mock,
        mock_valid_url: unittest.mock.Mock,
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Accessible"
        )

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_no_internet(
        self,
        mock_has_internet: unittest.mock.Mock,
        mock_valid_url: unittest.mock.Mock,
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Not accessible"
        )

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_invalid_url(
        self,
        mock_has_internet: unittest.mock.Mock,
        mock_valid_url: unittest.mock.Mock,
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        self.assertEqual(
            can_access_google_page("https://invalid-url.com"), "Not accessible"
        )

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_no_internet_and_invalid_url(
        self,
        mock_has_internet: unittest.mock.Mock,
        mock_valid_url: unittest.mock.Mock,
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = False
        self.assertEqual(
            can_access_google_page("https://invalid-url.com"), "Not accessible"
        )


if __name__ == "__main__":
    unittest.main()
