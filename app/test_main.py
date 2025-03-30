import unittest
from unittest import mock
from datetime import datetime
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_has_internet: bool,
                                    mock_valid_google_url: bool) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet.return_value = True
        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.datetime")
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_cannot_access_if_only_connection(self,
                                              mock_has_internet: bool,
                                              mock_valid_google_url: bool,
                                              mock_datetime: tuple) -> None:
        mock_valid_google_url.return_value = False
        mock_has_internet.return_value = True
        mock_datetime.now.return_value = datetime(2023, 7, 11, 12, 0, 0)
        result = can_access_google_page("https://www.example.com")

        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.datetime")
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_cannot_access_if_only_valid_url(self,
                                             mock_has_internet: bool,
                                             mock_valid_google_url: bool,
                                             mock_datetime: tuple) -> None:
        mock_valid_google_url.return_value = True
        mock_has_internet.return_value = False
        mock_datetime.now.return_value = datetime(2023, 7, 11, 23, 0, 0)
        result = can_access_google_page("https://www.google.com")

        self.assertEqual(result, "Not accessible")


if __name__ == "__main__":
    unittest.main()
