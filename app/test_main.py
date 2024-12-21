from typing import Any
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_called(
        mocked_has_internet_connection: Any
) -> None:
    can_access_google_page("https://google.com")
    mocked_has_internet_connection.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_called_with_correct_parameters(
        mocked_valid_google_url: Any
) -> None:
    can_access_google_page("https://google.com")
    mocked_valid_google_url.assert_called_once_with("https://google.com")
