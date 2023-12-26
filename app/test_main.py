from unittest import TestCase
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_accessible(
            self,
            mock_valid_url: MagicMock,
            mock_has_internet: MagicMock,
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        self.assertEqual(can_access_google_page("http://www.google.com"
                                                ), "Accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible_by_connection(
            self,
            mock_valid_url: MagicMock,
            mock_has_internet: MagicMock,
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True

        self.assertEqual(can_access_google_page("http://www.google.com"
                                                ), "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_not_accessible_by_url(
            self,
            mock_valid_url: MagicMock,
            mock_has_internet: MagicMock,
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False

        self.assertEqual(can_access_google_page("http://www.google.com"
                                                ), "Not accessible")
