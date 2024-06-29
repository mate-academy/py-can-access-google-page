import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_internet, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.invalidurl.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    url: str,
    valid_url: bool,
    has_internet: bool,
    expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    result = can_access_google_page(url)
    assert result == expected_result
