import pytest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage:

    @patch("app.main.valid_google_url")
    @patch("app.main.has_internet_connection")
    def test_can_access_google_page(self, mock_internet, mock_valid_url):
        test_cases = [
            (True, True, "Accessible"),
            (False, True, "Not accessible"),
            (True, False, "Not accessible"),
            (False, False, "Not accessible")
        ]

        for valid_url, internet, expected in test_cases:
            mock_valid_url.return_value = valid_url
            mock_internet.return_value = internet
            result = can_access_google_page("www.google.com")
            assert result == expected

if __name__ == "__main__":
    pytest.main()
