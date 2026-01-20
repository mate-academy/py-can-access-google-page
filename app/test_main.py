from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mock_valid_url, mock_internet_connection, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible",),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible")
    ],
    ids=[
        "valid_url_and_connection_exists",
        "invalid_url_and_connection_exists",
        "valid_url_and_no_connection",
        "invalid_url_and_no_connection"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
    url: str,
    mock_valid_url: bool,
    mock_internet_connection: bool,
    expected: str
) -> None:
    """
    Test can_access_google_page with various combinations of URL validity
    and internet connection.
    """
    mocked_valid_google_url.return_value = mock_valid_url
    mocked_has_internet_connection.return_value = mock_internet_connection

    assert can_access_google_page(url) == expected
