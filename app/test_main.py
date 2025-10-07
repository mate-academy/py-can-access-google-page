from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    """Test suite for can_access_google_page function."""

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_accessible_with_internet_and_valid_url(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test returns 'Accessible' when both conditions are met."""
        mock_internet.return_value = True
        mock_valid_url.return_value = True

        result = can_access_google_page("https://www.google.com")

        assert result == "Accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_called_once_with("https://www.google.com")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_without_internet(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test returns 'Not accessible' with no internet
        connection."""
        mock_internet.return_value = False
        mock_valid_url.return_value = True

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
        mock_internet.assert_called_once()

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_with_invalid_url(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test returns 'Not accessible' when URL is invalid."""
        mock_internet.return_value = True
        mock_valid_url.return_value = False

        result = can_access_google_page("https://invalid.url")

        assert result == "Not accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_called_once_with("https://invalid.url")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_without_internet_and_invalid_url(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test returns 'Not accessible' when both conditions
        fail."""
        mock_internet.return_value = False
        mock_valid_url.return_value = False

        result = can_access_google_page("https://invalid.url")

        assert result == "Not accessible"
        mock_internet.assert_called_once()

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_url_parameter_passed_correctly(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test URL parameter is passed correctly to
        valid_google_url."""
        mock_internet.return_value = True
        mock_valid_url.return_value = True

        test_url = "https://google.com/search"
        can_access_google_page(test_url)

        mock_valid_url.assert_called_once_with(test_url)

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_valid_url_not_called_without_internet(
        self,
        mock_valid_url: MagicMock,
        mock_internet: MagicMock
    ) -> None:
        """Test valid_google_url is not called when no internet
        (short-circuit)."""
        mock_internet.return_value = False

        result = can_access_google_page("https://www.google.com")

        assert result == "Not accessible"
        mock_internet.assert_called_once()
        # valid_google_url should not be called due to short-circuit
        mock_valid_url.assert_not_called()
