from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_functions_has_internet_connection_and_valid_google_url_were_called(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    can_access_google_page("https://www.google.com")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once()
