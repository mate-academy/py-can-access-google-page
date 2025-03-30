import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: None,
        mock_valid_google_url: None,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected: str
) -> None:

    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url

    address = "https://www.google.com"
    assert can_access_google_page(address) == expected
