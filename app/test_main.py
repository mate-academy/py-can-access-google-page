from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_scenarios(
        mock_valid: MagicMock,
        mock_inet: MagicMock,
        is_valid: bool,
        has_connection: bool,
        expected: str
) -> None:
    mock_valid.return_value = is_valid
    mock_inet.return_value = has_connection
    assert can_access_google_page("https://mate.academy/home") == expected
