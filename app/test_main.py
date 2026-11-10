from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url_valid, has_connection, expected",
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
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
    is_url_valid: bool,
    has_connection: bool,
    expected: str,
) -> None:
    """
    Test can_access_google_page with various combinations.

    Checks URL validity and internet connection.
    """
    mock_valid_url.return_value = is_url_valid
    mock_has_connection.return_value = has_connection

    result = can_access_google_page("https://www.google.com")
    assert result == expected
