import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "has_connection, is_valid, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url,
        mock_has_internet,
        has_connection: bool,
        is_valid: bool,
        expected: str,
) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet.return_value = has_connection

    result = can_access_google_page("https://fake-url.com")
    assert result == expected
