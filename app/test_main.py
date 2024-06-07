import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize("mock_internet,mock_valid,url,expected", [
    (True, True, "https://www.google.com", "Accessible"),
    (False, True, "https://www.safari.com", "Not accessible"),
    (True, False, "https://www.google.com", "Not accessible"),
    (False, False, "https://www.mate.com", "Not accessible")
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_check_access_page(mock_internet_connection: bool,
                           mock_valid_google_url: bool,
                           mock_internet: bool,
                           mock_valid: bool, url: str,
                           expected: str) -> None:

    mock_valid_google_url.return_value = mock_valid
    mock_internet_connection.return_value = mock_internet

    assert can_access_google_page(url) == expected
