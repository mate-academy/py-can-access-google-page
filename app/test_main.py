import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_accest_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com") == expected_result
