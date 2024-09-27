import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet_value, mock_valid_url_value, expected_result, url",
    [
        (True, True, "Accessible", "https://www.google.com"),  # Accessible page
        (False, True, "Not accessible", "https://www.google.com"),  # No internet
        (True, False, "Not accessible", "https://invalid-url.com"),  # Invalid URL
        (False, False, "Not accessible", "https://invalid-url.com"),  # No internet & invalid URL
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet, mock_valid_url,
                                mock_internet_value, mock_valid_url_value,
                                expected_result, url):
    mock_internet.return_value = mock_internet_value
    mock_valid_url.return_value = mock_valid_url_value

    result = can_access_google_page(url)
    assert result == expected_result
