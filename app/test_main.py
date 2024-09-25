import pytest

from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet, mock_valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url_func: patch,
        mock_internet_func: patch,
        mock_internet: bool,
        mock_valid_url: bool,
        expected_result: str
) -> None:
    mock_internet_func.return_value = mock_internet
    mock_valid_url_func.return_value = mock_valid_url

    assert can_access_google_page("http://google.com") == expected_result
