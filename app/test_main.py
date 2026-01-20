import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, result", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: any,
        mock_valid_google_url: any,
        has_internet_connection: callable,
        valid_google_url: callable, result: str
) -> any:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("http://google.com") == result
