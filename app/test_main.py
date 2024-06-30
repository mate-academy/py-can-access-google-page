from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_google_url_return, "
    "mock_has_internet_connection_return, "
    "expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: patch,
        mock_valid_google_url: patch,
        mock_valid_google_url_return: bool,
        mock_has_internet_connection_return: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = mock_valid_google_url_return
    mock_has_internet.return_value = mock_has_internet_connection_return
    assert can_access_google_page("http://www.google.com") == expected
