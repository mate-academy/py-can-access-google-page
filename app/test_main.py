from unittest.mock import patch
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_conn, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url,
    mock_has_internet_connection,
    valid_url,
    internet_conn,
    expected,
):
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_conn

    result = can_access_google_page("https://www.google.com")
    
    assert result == expected
    
    # Перевіряємо виклики з урахуванням логіки Python (короткого замикання)
    mock_has_internet_connection.assert_called_once()
    
    if internet_conn:
        mock_valid_google_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_google_url.assert_not_called()