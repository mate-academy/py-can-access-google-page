import unittest
from unittest import mock

import app.main


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_accessible(
            self,
            mock_valid_url: bool,
            mock_has_internet: bool
    ) -> None:
        mock_valid_url.return_value = True
        mock_has_internet.return_value = True
        result = app.main.can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_valid_url: bool,
            mock_has_internet: bool
    ) -> None:
        mock_valid_url.return_value = False
        mock_has_internet.return_value = True
        result = app.main.can_access_google_page("https://www.invalidurl.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_not_accessible_due_to_no_internet_connection(
            self,
            mock_valid_url: bool,
            mock_has_internet: bool
    ) -> None:
        mock_valid_url.return_value = True
        mock_has_internet.return_value = False
        result = app.main.can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_not_accessible_due_to_invalid_url_and_no_internet_connection(
            self,
            mock_valid_url: bool,
            mock_has_internet: bool
    ) -> None:
        mock_valid_url.return_value = False
        mock_has_internet.return_value = False
        result = app.main.can_access_google_page("https://www.invalidurl.com")
        self.assertEqual(result, "Not accessible")
