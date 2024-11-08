import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_return, internet_return, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.full-sheet-url.co", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.full-sheet-url.co", False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet: patch,
        mock_valid_url: patch,
        url: str,
        valid_url_return: bool,
        internet_return: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = valid_url_return
    mock_internet.return_value = internet_return

    result = can_access_google_page(url)
    assert result == expected_result
