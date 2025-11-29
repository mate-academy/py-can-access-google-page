import pytest

from unittest import mock
import app.maim as main

from main import can_access_google_page

@pytest.mark.parametrize("arg1 , arg2, expected",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible")
                         ]
                         )
@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: object,
        mock_valid_google_url: object,
        arg1: bool,
        arg2: bool,
        expected: bool) -> None:
    mock_has_internet_connection.return_value = arg1
    mock_valid_google_url.return_value = arg2
    assert (main.can_access_google_page("http//:googlecom") == expected)