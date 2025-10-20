import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_return, internet_return, expected_result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        url: str,
        valid_url_return: bool,
        internet_return: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_return
    mock_valid_google_url.return_value = valid_url_return
    result = can_access_google_page(url)
    assert result == expected_result
