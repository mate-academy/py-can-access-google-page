from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "mock_valid_google_url, mock_has_internet_connection, end_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_google_page(mock_valid_google_url: str,
                     mock_has_internet_connection: str,
                     end_result: str) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=mock_valid_google_url):
        with mock.patch("app.main.has_internet_connection",
                        return_value=mock_has_internet_connection):
            result = can_access_google_page("http://www.google.com")
            assert result == end_result
