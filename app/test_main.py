import pytest
from unittest.mock import patch, Mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://notvalidgoogle.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://notvalidgoogle.com", False, False, "Not accessible"),
    ],
    ids=[
        "Valid URL with internet connection - should be accessible",
        "Invalid URL with internet connection - should not be accessible",
        "Valid URL without internet connection - should not be accessible",
        "Invalid URL and no internet connection - should not be accessible",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: Mock,
    mock_valid_url: Mock,
    url: str,
    valid_url: bool,
    internet_connection: bool,
    expected_result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page(url) == expected_result
