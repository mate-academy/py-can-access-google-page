from unittest.mock import patch
from app.main import can_access_google_page
from unittest.mock import MagicMock


class TestCanAccessGooglePage:

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True
        url = "https://www.google.com"

        # Act
        result = can_access_google_page(url)

        # Assert
        assert result == "Accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_internet(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True
        url = "https://www.google.com"

        result = can_access_google_page(url)

        assert result == "Not accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_not_accessible_due_to_invalid_url(
            self,
            mock_has_internet: MagicMock,
            mock_valid_url: MagicMock
    ) -> None:
        mock_has_internet.return_value = True
        mock_valid_url.return_value = False
        url = "https://invalid-url.com"

        result = can_access_google_page(url)

        assert result == "Not accessible"
