import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "url, internet_connection, valid_url, expected_result",
    [
        ("https://google.com", True, True, "Accessible"),  # Valid URL and has internet
        ("https://google.com", False, True, "Not accessible"),  # No internet
        ("https://invalidsite.com", True, False, "Not accessible"),  # Invalid URL
        ("https://invalidsite.com", False, False, "Not accessible"),  # Both invalid URL and no internet
        ("", True, False, "Not accessible"),  # Empty URL
    ],
)
def test_can_access_google_page(url, internet_connection, valid_url, expected_result):
    with patch("app.main.has_internet_connection", return_value=internet_connection), \
         patch("app.main.valid_google_url", return_value=valid_url):
        result = can_access_google_page(url)
        assert result == expected_result
