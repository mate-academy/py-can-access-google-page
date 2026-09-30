from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_accessible_when_url_valid_and_has_internet(
        self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        # Arrange
        mock_url.return_value = True
        mock_internet.return_value = True
        # Act
        result = can_access_google_page("https://www.google.com")
        # Assert
        assert result == "Accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_url_valid_and_no_internet(
            self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        # Arrange
        mock_url.return_value = True
        mock_internet.return_value = False
        # Act
        result = can_access_google_page("https://www.google.com")
        # Assert
        assert result == "Not accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_url_invalid_and_has_internet(
            self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        # Arrange
        mock_url.return_value = False
        mock_internet.return_value = True
        # Act
        result = can_access_google_page("https://www.google.com")
        # Assert
        assert result == "Not accessible"

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_url_invalid_and_no_internet(
            self, mock_internet: MagicMock, mock_url: MagicMock
    ) -> None:
        # Arrange
        mock_url.return_value = False
        mock_internet.return_value = False
        # Act
        result = can_access_google_page("https://www.google.com")
        # Assert
        assert result == "Not accessible"
