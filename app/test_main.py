# write your code here
import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url, internet_connection, access_status",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_if_accesible(mock_valid_url: mock.Mock,
                      mock_has_internet_connection: mock.Mock,
                      url: bool,
                      internet_connection: bool,
                      access_status: str) -> None:
    mock_valid_url.return_value = url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == access_status
