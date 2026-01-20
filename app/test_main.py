from unittest import TestCase
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
class TestCanAccessGooglePage(TestCase):

    def test_accessible(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        # Arrange
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        url = "https://www.google.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Accessible")

    def test_not_accessible_due_to_internet(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        url = "https://www.google.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Not accessible")

    def test_not_accessible_due_to_invalid_url(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        url = "https://invalid-url.com"

        result = can_access_google_page(url)

        self.assertEqual(result, "Not accessible")
