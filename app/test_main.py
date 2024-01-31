from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "initial_address,expected_access,valid_google_url,has_internet_connection",
    [
        ("https://www.google.com", "Accessible", True, True),
        ("https://invalidurl.com", "Not accessible", False, True),
        ("https://www.google.com", "Not accessible", True, False),
        ("https://invalidurl.com", "Not accessible", False, False)
    ],
    ids=[
        "accessible correct url and has internet connection",
        "not accessible incorrect url",
        "not accessible no internet connection",
        "not accessible no connection and incorrect url",
    ]
)
def test_can_access_google_page(
        initial_address: str,
        expected_access: str,
        valid_google_url: bool,
        has_internet_connection: bool
) -> None:
    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        mock_valid_google_url.return_value = valid_google_url
        mock_has_internet_connection.return_value = has_internet_connection

        assert can_access_google_page(initial_address) == expected_access
