import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, valid_url, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://invalidurl.com", True, False, "Not accessible"),
        ("https://invalidurl.com", False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: bool,
                                mock_valid_google_url: bool,
                                url: str,
                                internet_connection: bool,
                                valid_url: bool,
                                expected_result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    result = can_access_google_page(url)

    assert result == expected_result
