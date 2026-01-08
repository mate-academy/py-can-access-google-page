from unittest.mock import patch, MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, is_valid_url, has_internet, expected_result",
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
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
    url: str,
    is_valid_url: bool,
    has_internet: bool,
    expected_result: str
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet.return_value = has_internet
    assert can_access_google_page(url) == expected_result
