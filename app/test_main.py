import pytest
from unittest.mock import patch
from typing import Any
from app.main import can_access_google_page


@pytest.mark.parametrize("internet, valid_url, url, expected", [
    (False, True, "https://www.google.com", "Not accessible"),
    (True, False, "https://invalid-url.com", "Not accessible"),
    (True, True, "https://www.google.com", "Accessible")
])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: Any,
                                mock_valid_google_url: Any,
                                internet: bool, valid_url: bool,
                                url: str, expected: str) -> None:
    mock_has_internet_connection.return_value = internet
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected


if __name__ == "__main__":
    pytest
