from unittest.mock import MagicMock, patch
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected_result",
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
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
    has_internet: bool,
    valid_url: bool,
    expected_result: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url

    result = can_access_google_page("https://www.google.com")

    assert result == expected_result
    mock_has_internet.assert_called_once()
    if has_internet:
        mock_valid_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_url.assert_not_called()
