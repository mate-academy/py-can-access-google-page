import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_accessible(
            self,
            mock_internet_connection: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock,
    ) -> None:

        mock_internet_connection.return_value = True
        mock_valid_url.return_value = True
        url = "http://www.example.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Accessible")


class TestCanAccessInternet(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=False)
    @patch("app.main.has_internet_connection", return_value=True)
    def test_access_google_page_not_valid_url(
            self,
            mock_internet_connection: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock,
    ) -> None:

        mock_internet_connection.return_value = False
        mock_valid_url.return_value = True
        url = "http://www.example.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Not accessible")


class TestCanAccessValidURL(unittest.TestCase):

    @patch("app.main.valid_google_url", return_value=True)
    @patch("app.main.has_internet_connection", return_value=False)
    def test_access_google_page_not_internet_connection(
            self,
            mock_internet_connection: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock,
    ) -> None:

        mock_internet_connection.return_value = True
        mock_valid_url.return_value = False
        url = "http://www.example.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Not accessible")
