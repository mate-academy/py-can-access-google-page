import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_is_valid, has_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url_is_valid: bool,
    has_connection: bool,
    expected: str,
) -> None:
    """Test can_access_google_page behavior with mocked dependencies."""
    with patch(
        "app.main.valid_google_url", return_value=url_is_valid
    ), patch(
        "app.main.has_internet_connection", return_value=has_connection
    ):
        result: str = can_access_google_page("https://google.com")
        assert result == expected
