import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url, mock_internet, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_url_func: bool,
                                mock_internet_conn: bool,
                                mock_valid_url: bool, mock_internet: bool,
                                expected: str) -> None:
    mock_valid_url_func.return_value = mock_valid_url
    mock_internet_conn.return_value = mock_internet
    result = can_access_google_page("https://www.google.com")
    assert result == expected, f"Expected {expected}, but got {result}"
