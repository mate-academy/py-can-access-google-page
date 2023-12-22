import pytest
from unittest.mock import patch
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result, url",
    [
        (True, True, "Accessible", "https://www.google.com"),
        (False, True, "Not accessible", "https://www.google.com"),
        (True, False, "Not accessible", "https://www.guagle.com"),
        (False, False, "Not accessible", "invalid_url"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: Callable,
        mock_has_internet_connection: Callable,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str,
        url: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page(url)
    assert result == expected_result


if __name__ == "__main__":
    pytest.main()
