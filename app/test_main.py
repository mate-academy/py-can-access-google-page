import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, is_valid, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    has_internet: bool,
    is_valid: bool,
    expected_result: str
) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet_connection.return_value = has_internet

    result = can_access_google_page("http://www.google.com")

    assert result == expected_result
