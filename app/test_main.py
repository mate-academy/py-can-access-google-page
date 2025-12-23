from unittest import mock
import pytest
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize("has_internet, is_valid_url, expected", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],)
    def test_can_access_google_page(self,
                                    has_internet: bool,
                                    is_valid_url: bool,
                                    expected: str) -> None:
        with (mock.patch("app.main.valid_google_url")
              as mock_valid_google_url,
              mock.patch("app.main.has_internet_connection")
              as mock_has_internet_connection):
            mock_valid_google_url.return_value = is_valid_url
            mock_has_internet_connection.return_value = has_internet
            result = can_access_google_page("https://google.com")
            assert result == expected
            if has_internet:
                mock_valid_google_url.assert_called_once_with(
                    "https://google.com")
            else:
                mock_valid_google_url.assert_not_called()
            mock_has_internet_connection.assert_called_once()
