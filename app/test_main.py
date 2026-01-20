import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
    ],
    ids=[
        "valid_and_connected",
        "invalid_url_and_connected",
        "valid_url_and_not_connected"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet: MagicMock, mock_url: MagicMock,
    url: str, valid_url: bool, internet_connection: bool, expected_result: str
) -> None:

    mock_url.return_value = valid_url
    mock_internet.return_value = internet_connection
    assert can_access_google_page(url) == expected_result
