import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(mock_url: str,
                                mock_connection: str, valid_url: str,
                                has_connection: str, expected: bool) -> None:
    mock_url.return_value = valid_url
    mock_connection.return_value = has_connection

    result = can_access_google_page("https://google.com")
    assert result == expected
