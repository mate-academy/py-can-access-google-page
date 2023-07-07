from typing import Callable
from unittest import mock

from .main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_accessible(
        mocked_int_connect: Callable,
        mocked_valid_url: Callable
) -> None:
    mocked_int_connect.return_value = True
    mocked_valid_url.return_value = True
    can_access_google_page("https://www.google.com")

    mocked_int_connect.assert_called_once()
    mocked_valid_url.assert_called_once_with(
        "https://www.google.com"
    )
