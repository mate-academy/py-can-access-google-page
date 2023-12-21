import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection, mock_valid_google_url):
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    result = can_access_google_page("invalid_url")
    assert result == "Not accessible"


if __name__ == "__main__":
    pytest.main()
