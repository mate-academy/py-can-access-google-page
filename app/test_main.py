import unittest
from unittest import mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_has_internet_connection_and_valid_google_url(
            self,
            mock_has_internet_connection: mock,
            mock_valid_google_url: mock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_has_no_internet_connection(
            self,
            mock_has_internet_connection: mock,
            mock_valid_google_url: mock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_invalid_google_url(
            self,
            mock_has_internet_connection: mock,
            mock_valid_google_url: mock
    ) -> None:
        mock_has_internet_connection.return_value = True
        mock_valid_google_url.return_value = False

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_no_internet_connection_and_invalid_google_url(
            self,
            mock_has_internet_connection: mock,
            mock_valid_google_url: mock
    ) -> None:
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = False

        result = can_access_google_page("https://invalid.url")
        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
