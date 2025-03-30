from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.invalid-google_serv.com")
    assert result == "Not accessible"

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
