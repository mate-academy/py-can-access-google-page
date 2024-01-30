from unittest.mock import patch, Mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,valid_google_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        has_internet: bool,
        valid_google_url: bool,
        expected: str
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("www.google.com") == expected
