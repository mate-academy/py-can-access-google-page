import pytest
from unittest.mock import patch, Mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_connection: Mock,
    mock_url: Mock,
    url_valid: bool,
    internet: bool,
    expected: str,
) -> None:
    mock_url.return_value = url_valid
    mock_connection.return_value = internet

    result = can_access_google_page("https://google.com")
    assert result == expected
