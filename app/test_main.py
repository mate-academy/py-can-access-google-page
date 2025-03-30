import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet: bool,
                                mock_valid_url: bool,
                                url: bool,
                                valid_url: bool,
                                internet_connection: bool,
                                expected_result: str) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet.return_value = internet_connection

    result = can_access_google_page(url)
    assert result == expected_result
