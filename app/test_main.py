import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "mock_valid_google_url, mock_has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(mock_valid_google_url, mock_has_internet_connection, expected):
    with patch("app.main.valid_google_url", return_value=mock_valid_google_url), \
         patch("app.main.has_internet_connection", return_value=mock_has_internet_connection):
        assert can_access_google_page("https://www.google.com") == expected
