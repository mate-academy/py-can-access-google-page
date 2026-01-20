from pytest import mark
from unittest import mock

from app.main import can_access_google_page


URL = "https://www.google.com"


@mark.parametrize(
    "connected, valid_url, can_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "if url is valid and it has internet connection, return 'Accessible'",
        "if it hasn't internet connection, return 'Not accessible'",
        "if url is not valid, must return 'Not accessible'",
        "if url isn't valid and no connection, return 'Not accessible'"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_has_internet_connection: mock,
    mock_valid_google_url: mock,
    connected: bool,
    valid_url: bool,
    can_access: str
) -> None:
    mock_has_internet_connection.return_value = connected
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page(URL) == can_access
