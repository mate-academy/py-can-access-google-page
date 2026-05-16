import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch('app.main.has_internet_connection')  # ближче до функції
@patch('app.main.valid_google_url')
def test_can_access_google_page(mock_url, mock_connection, valid_url, has_connection, expected):
    mock_url.return_value = valid_url
    mock_connection.return_value = has_connection

    result = can_access_google_page("https://google.com")
    assert result == expected
