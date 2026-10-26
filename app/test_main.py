from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_return, internet_return, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
    url: str,
    valid_url_return: bool,
    internet_return: bool,
    expected_result: str,
) -> None:
    mock_valid_google_url.return_value = valid_url_return
    mock_has_internet_connection.return_value = internet_return

    result = can_access_google_page(url)

    assert result == expected_result
    mock_has_internet_connection.assert_called_once()

    if internet_return:
        mock_valid_google_url.assert_called_once_with(url)
    else:
        mock_valid_google_url.assert_not_called()
