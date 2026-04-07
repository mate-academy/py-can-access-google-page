from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_scenarios(
        mock_internet: MagicMock,
        mock_valid: MagicMock,
        valid: bool,
        internet: bool,
        expected: str
) -> None:
    mock_internet.return_value = internet
    mock_valid.return_value = valid
    result = can_access_google_page("google.com")
    assert result == expected
