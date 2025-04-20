from app.main import can_access_google_page
import pytest
from unittest.mock import MagicMock, patch


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_internet: MagicMock,
    mock_valid_url: MagicMock,
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    """
    Test can_access_google_page() by mocking valid_google_url and
    has_internet_connection to simulate all access scenarios.
    """
    mock_internet.return_value = internet
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("http://google.com") == expected
