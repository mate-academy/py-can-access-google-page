from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("param1, param2, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_main_can_access_google_page(
                                     mock_has_internet_connection: bool,
                                     mock_valid_google_url: bool,
                                     param1: bool,
                                     param2: bool, expected: str) -> None:
    mock_has_internet_connection.return_value = param1
    mock_valid_google_url.return_value = param2
    result = can_access_google_page("https://www.google.com")
    assert result == expected
