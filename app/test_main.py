from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page
from unittest.mock import patch


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_functions_has_internet_connection_and_valid_google_url_were_called(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
) -> None:
    can_access_google_page("https://www.google.com")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once()


@pytest.mark.parametrize(
    "internet, valid_url, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_accessible_address_has_internet_connection(
        internet: bool,
        valid_url: bool,
        result: str
) -> None:
    with (patch("app.main.has_internet_connection")
          as mocked_has_internet_connection,
            patch("app.main.valid_google_url") as mocked_valid_google_url):
        mocked_has_internet_connection.return_value = internet
        mocked_valid_google_url.return_value = valid_url
        assert can_access_google_page("some.address") == result
