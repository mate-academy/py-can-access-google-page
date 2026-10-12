from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
    has_connection: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = has_connection
    mock_valid_url.return_value = is_valid_url

    assert can_access_google_page("https://google.com") == expected
