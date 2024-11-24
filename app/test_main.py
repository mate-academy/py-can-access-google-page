import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "mock_internet, mock_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url,
        mock_has_internet_connection,
        mock_internet,
        mock_url,
        expected
):

    mock_has_internet_connection.return_value = mock_internet
    mock_valid_google_url.return_value = mock_url

    result = can_access_google_page("https://www.google.com")

    assert result == expected
