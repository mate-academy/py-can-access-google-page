import unittest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_accessible_when_valid_url_and_internet(
            self,
            mock_internet: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock
    ) -> None:
        mock_internet.return_value = True
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Accessible"
        )

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_not_accessible_when_no_internet(
            self,
            mock_internet: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock
    ) -> None:
        mock_internet.return_value = False
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("https://www.google.com"), "Not accessible"
        )

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_not_accessible_when_not_valid_url(
            self,
            mock_internet: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock
    ) -> None:
        mock_internet.return_value = True
        mock_valid_url.return_value = False
        self.assertEqual(
            can_access_google_page("https://www.google"), "Not accessible"
        )

    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_not_accessible_when_not_valid_url_and_no_internet(
            self,
            mock_internet: unittest.mock.Mock,
            mock_valid_url: unittest.mock.Mock
    ) -> None:
        mock_internet.return_value = False
        mock_valid_url.return_value = False
        self.assertEqual(
            can_access_google_page("https://www.google"), "Not accessible"
        )
