import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "net_connection, valid_url, is_connection",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Everything works!",
        "With internet connection, but invalid url.",
        "Without internet connection, but url is valid.",
        "No internet connection and invalid url."
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock,
        net_connection: bool,
        valid_url: bool,
        is_connection: str
) -> None:
    mock_has_internet_connection.return_value = net_connection
    mock_valid_google_url.return_value = valid_url
    assert (can_access_google_page("https://www.google.com") == is_connection)
