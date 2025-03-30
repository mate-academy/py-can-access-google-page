import unittest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page(
        self,
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://google.com"), "Accessible"
        )

    @mock.patch("app.main.valid_google_url", return_value=False)
    @mock.patch("app.main.has_internet_connection", return_value=True)
    def test_can_access_google_page_invalid_url(
        self,
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://invalidurl.com"), "Not accessible"
        )

    @mock.patch("app.main.valid_google_url", return_value=True)
    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_can_access_google_page_no_internet_connection(
        self,
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
    ) -> None:
        self.assertEqual(
            can_access_google_page("https://google.com"), "Not accessible"
        )
