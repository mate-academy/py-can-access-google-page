import pytest
from unittest import mock
from main import can_access_google_page


@pytest.mark.parametrize(
    "connected, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(connected, valid_url, expected):
    with mock.patch("main.has_internet_connection") as mock_connection:
        with mock.patch("main.valid_google_url") as mock_valid:
            mock_connection.return_value = connected
            mock_valid.return_value = valid_url

            result = can_access_google_page("https://google.com")

            assert result == expected
