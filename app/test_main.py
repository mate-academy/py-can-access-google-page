from unittest import mock

import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("mock_internet,mock_valid,url, expected", [
    (True, True, "https://www.google.com", "Accessible"),
    (False, True, "https://www.example.com", "Not accessible"),
    (True, False, "https://www.google.com", "Not accessible"),
    (False, False, "https://www.example.com", "Not accessible"),

])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_internet_connection: any,
                                mock_valid_google_url: any,
                                mock_internet: bool, mock_valid: bool,
                                url: str, expected: str) -> None:
    mock_internet_connection.return_value = mock_internet
    mock_valid_google_url.return_value = mock_valid
    assert can_access_google_page(url) == expected
