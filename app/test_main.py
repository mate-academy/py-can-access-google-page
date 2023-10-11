import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.test_main.valid_google_url")
@patch("app.test_main.has_internet_connection")
@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", "Accessible"),
    ("https://www.google.ru", "Accessible"),
    ("https://www.google.co.jp", "Accessible"),
    ("https://www.yahoo.com", "Not accessible"),
    ("https://www.bing.com", "Not accessible"),
])
def test_can_access_google_page(mock_internet_connection, mock_valid_google_url, url, expected_result):
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True
    actual_result = can_access_google_page(url)

    assert actual_result == expected_result
