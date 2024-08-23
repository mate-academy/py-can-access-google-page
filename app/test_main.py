import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    valid_url: bool,
    has_connection: bool,
    expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection
    url = "https://www.test-url.com"
    assert can_access_google_page(url) == expected_result
