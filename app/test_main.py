import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_status, url_status, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_combinations(
        mock_internet: MagicMock,
        mock_url: MagicMock,
        internet_status: bool,
        url_status: bool,
        expected_result: str,
) -> None:
    mock_url.return_value = url_status
    mock_internet.return_value = internet_status
    result = can_access_google_page("https://google.com")
    assert result == expected_result
