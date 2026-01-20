import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet, mock_url, url, expected_result",
    [
        (True, True,
         "https://www.google.com", "Accessible"),  # Valid all
        (True, False,
         "https://www.invalid-url.com", "Not accessible"),  # Invalid URL
        (False, True,
         "https://www.google.com", "Not accessible"),  # Invalid internet
        (False, False,
         "https://www.invalid-url.com", "Not accessible"),  # Invalid all
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet_connection: patch,
        mock_valid_url: patch,
        mock_internet: bool,
        mock_url: bool,
        url: str,
        expected_result: str
) -> None:
    mock_internet_connection.return_value = mock_internet
    mock_valid_url.return_value = mock_url

    result = can_access_google_page(url)
    assert result == expected_result
