import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_status, url_status, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: MagicMock,
        mock_valid_url: MagicMock,
        internet_status: bool,
        url_status: bool,
        expected_result: str
) -> None:
    mock_has_internet.return_value = internet_status
    mock_valid_url.return_value = url_status
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
