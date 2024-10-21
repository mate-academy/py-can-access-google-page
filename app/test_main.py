import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected_result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: patch,
        mock_has_internet_connection: patch,
        valid_url: bool,
        has_connection: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
