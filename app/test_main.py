import unittest
from unittest.mock import patch, Mock
from app.main import can_access_google_page


class TestAccessGooglePage(unittest.TestCase):

    @patch("app.main.has_internet_connection", return_value=False)
    @patch("app.main.valid_google_url", return_value=True)
    def test_cannot_access_if_only_valid_url(
            self,
            mock_valid_google_url: Mock,
            mock_has_internet_connection: Mock
    ) -> None:
        self.assertEqual(
            can_access_google_page("http://www.google.com"), "Not accessible"
        )

    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=False)
    def test_cannot_access_if_only_connection(
            self,
            mock_valid_google_url: Mock,
            mock_has_internet_connection: Mock
    ) -> None:
        self.assertEqual(
            can_access_google_page("http://www.google.com"), "Not accessible"
        )

    @patch("app.main.has_internet_connection", return_value=True)
    @patch("app.main.valid_google_url", return_value=False)
    def test_cannot_access_if_connection_or_valid_url_is_true(
            self,
            mock_valid_google_url: Mock,
            mock_has_internet_connection: Mock
    ) -> None:
        self.assertEqual(
            can_access_google_page("http://www.google.com"), "Not accessible"
        )
        mock_has_internet_connection.return_value = False
        mock_valid_google_url.return_value = True
        self.assertEqual(
            can_access_google_page("http://www.google.com"), "Not accessible"
        )
