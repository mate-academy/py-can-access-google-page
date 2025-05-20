from unittest import TestCase
from unittest.mock import patch, Mock
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_accessible_when_url_valid_and_has_connection(
        self, mock_valid_url: Mock, mock_has_connection: Mock
    ) -> None:
        mock_valid_url.return_value = True
        mock_has_connection.return_value = True
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_when_url_invalid(
        self, mock_valid_url: Mock, mock_has_connection: Mock
    ) -> None:
        mock_valid_url.return_value = False
        mock_has_connection.return_value = True
        result = can_access_google_page("https://notgoogle.com")
        self.assertEqual(result, "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_when_no_connection(
        self, mock_valid_url: Mock, mock_has_connection: Mock
    ) -> None:
        mock_valid_url.return_value = True
        mock_has_connection.return_value = False
        result = can_access_google_page("https://www.google.com")
        self.assertEqual(result, "Not accessible")
