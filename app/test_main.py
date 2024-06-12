import pytest
from unittest import mock
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "url, has_connection, is_valid_url, expected_result",
    [
        # Valid URL cases
        ("https://google.com", True, True, "Accessible"),
        ("http://google.com", True, True, "Accessible"),
        ("https://google.com?q=test", True, True, "Accessible"),
        # Invalid URL cases
        ("", True, False, "Not accessible"),
        ("https://g@ogle.com", True, False, "Not accessible"),
        ("https://www", True, False, "Not accessible"),
        # Connection cases
        ("https://google.com", False, True, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        url: str,
        has_connection: bool,
        is_valid_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_connection
    mock_valid_google_url.return_value = is_valid_url
    result = can_access_google_page(url)
    assert result == expected_result
