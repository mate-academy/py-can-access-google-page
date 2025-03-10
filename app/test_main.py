from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url,is_valid_url,has_internet_connection,expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google", False, True, "Not accessible"),
        ("https://amazon.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable,
        url: str,
        is_valid_url: bool,
        has_internet_connection: bool,
        expected: str,
) -> None:
    mocked_valid_google_url.return_value = is_valid_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page(url) == expected
