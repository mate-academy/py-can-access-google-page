import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.fakegoogle.com", False, True, "Not accessible"),
        ("https://www.fakegoogle.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
    url: str,
    valid_url: bool,
    internet_connection: bool,
    expected_result: str
) -> None:
    with (patch("app.main.valid_google_url") as mocked_valid_url,
         patch("app.main.has_internet_connection") as
         mocked_internet_connection):
        mocked_valid_url.return_value = valid_url
        mocked_internet_connection.return_value = internet_connection
        result = can_access_google_page(url)
        assert result == expected_result
