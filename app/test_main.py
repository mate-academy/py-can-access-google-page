import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_internet_connection, valid_url, expected_output",
    [
        ("https://mail.google.com/mail/", True, False, "Not accessible"),
        ("https://mate.academy", False, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", True, True, "Accessible"),
    ],
    ids=[
        "'Not accessible' url is not valid",
        "'Not accessible' no internet connection and url is not valid",
        "'Not accessible' no internet connection",
        "'Accessible' url is valid and have internet connection",
    ]
)
def test_can_access_google_page(url: str,
                                has_internet_connection: bool,
                                valid_url: bool,
                                expected_output: str) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=valid_url), \
         mock.patch("app.main.has_internet_connection",
                    return_value=has_internet_connection):
        result = can_access_google_page(url)
        assert result == expected_output
