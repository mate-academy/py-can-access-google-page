from unittest import TestCase
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestGoogleAccess(TestCase):

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("some address"), "Accessible"
        )
        mock_valid_url.return_value = False
        self.assertEqual(
            can_access_google_page("some address"), "Not accessible"
        )
        mock_has_internet.return_value = False
        self.assertEqual(
            can_access_google_page("some address"), "Not accessible"
        )
        mock_valid_url.return_value = True
        self.assertEqual(
            can_access_google_page("some address"), "Not accessible"
        )
