import pytest
from unittest.mock import Mock, patch
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "mock_valid_url, mock_internet_connection, expected",
        [
            pytest.param(
                True, True, "Accessible",
                id="URL and internet connection are valid"
            ),
            pytest.param(
                True, False, "Not accessible",
                id="Valid URL but no internet connection"
            ),
            pytest.param(
                False, True, "Not accessible",
                id="Invalid URL but internet connection"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="Invalid URL and no internet connection"
            ),
        ]
    )
    @patch('app.main.valid_google_url')
    @patch('app.main.has_internet_connection')
    def test_can_access_google_page(
            self,
            mock_has_internet_connection: Mock,
            mock_valid_google_url: Mock,
            mock_valid_url: bool,
            mock_internet_connection: bool,
            expected: str
    ) -> None:
        mock_valid_google_url.return_value = mock_valid_url
        mock_has_internet_connection.return_value = mock_internet_connection
        result = can_access_google_page("http://google.com")
        assert result == expected
