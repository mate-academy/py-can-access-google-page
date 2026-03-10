from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid,conn,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access(
        mock_inet: MagicMock,
        mock_valid: MagicMock,
        valid: bool,
        conn: bool,
        expected: str
) -> None:
    mock_valid.return_value = valid
    mock_inet.return_value = conn
    assert can_access_google_page("https://mate.academy/home") == expected
