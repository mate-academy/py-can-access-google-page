from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_accessible_when_both_conditions_true(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:
        mock_internet.return_value = True
        mock_valid_url.return_value = True
        test_url = "https://www.google.com"

        result = can_access_google_page(test_url)

        assert result == "Accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_called_once_with(test_url)

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_when_no_internet(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = False
        mock_valid_url.return_value = True
        test_url = "https://www.google.com"

        result = can_access_google_page(test_url)

        assert result == "Not accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_not_called()

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_when_invalid_url(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        test_url = "https://invalid.url"

        result = can_access_google_page(test_url)

        assert result == "Not accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_called_once_with(test_url)

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_not_accessible_when_both_conditions_false(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = False
        mock_valid_url.return_value = False
        test_url = "https://invalid.url"

        result = can_access_google_page(test_url)

        assert result == "Not accessible"
        mock_internet.assert_called_once()
        mock_valid_url.assert_not_called()

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_url_passed_to_valid_google_url(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = True
        mock_valid_url.return_value = True
        test_url = "https://www.google.com"

        can_access_google_page(test_url)

        mock_valid_url.assert_called_once_with(test_url)

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_empty_url(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        test_url = ""

        result = can_access_google_page(test_url)

        assert result == "Not accessible"
        mock_valid_url.assert_called_once_with(test_url)

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_none_url(
            self,
            mock_valid_url: MagicMock,
            mock_internet: MagicMock
    ) -> None:

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        test_url = None

        result = can_access_google_page(test_url)

        assert result == "Not accessible"
        mock_valid_url.assert_called_once_with(test_url)
