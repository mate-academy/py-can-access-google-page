import pytest
from unittest.mock import Mock, patch


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        ("https://www.google.com", True, "Accessible"),
        ("https://www.google.com", False, "Not accessible"),
        ("https://www.invalidurl.com", True, "Not accessible"),
        ("https://www.invalidurl.com", False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock,
        valid_url: str,
        has_internet: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = \
        True if valid_url == "https://www.google.com" else False
    mock_has_internet_connection.return_value = has_internet

    assert can_access_google_page(valid_url) == expected_result
