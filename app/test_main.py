import pytest
from unittest.mock import MagicMock
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_available, expected_result, url_called",
    [
        (True, True, "Accessible", True),
        (False, True, "Not accessible", True),
        (True, False, "Not accessible", False)
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        valid_url: bool,
        internet_available: bool,
        expected_result: str,
        url_called: bool
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_available
    url = "https://www.google.com"
    result = can_access_google_page(url)

    assert result == expected_result

    if url_called:
        mock_valid_google_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_google_url.assert_not_called()

    mock_has_internet_connection.assert_called_once()
