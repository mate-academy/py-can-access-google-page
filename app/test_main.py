import pytest
from unittest.mock import patch, MagicMock
import app.main


@pytest.mark.parametrize(
    "has_internet, is_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: MagicMock,
        mock_valid_url: MagicMock,
        has_internet: bool,
        is_valid_url: bool,
        expected: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = is_valid_url

    result = app.main.can_access_google_page("https://google.com")

    assert result == expected
