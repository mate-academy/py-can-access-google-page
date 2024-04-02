import unittest
from unittest.mock import patch
from app import main


class TestCanAccessGooglePage(unittest.TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_accessible(
            self,
            mock_has_internet_connection: unittest.mock.Mock,
            mock_valid_google_url: unittest.mock.Mock) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        result = main.can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_not_accessible_invalid_url(
            self,
            mock_has_internet_connection: unittest.mock.Mock,
            mock_valid_google_url: unittest.mock.Mock) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        result = main.can_access_google_page("https://www.invalidurl.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page_not_accessible_no_internet(
            self,
            mock_has_internet_connection: unittest.mock.Mock,
            mock_valid_google_url: unittest.mock.Mock) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        result = main.can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    import subprocess
    subprocess.check_call(["pip", "install", "requests"])
