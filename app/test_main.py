from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_url, expected_output",
    [
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "'Not accessible' url is not valid",
        "'Not accessible' no internet connection and url is not valid",
        "'Not accessible' no internet connection",
        "'Accessible' url is valid and have internet connection",
    ]
)
def test_can_access_google_page(has_internet_connection: bool,
                                valid_url: bool,
                                expected_output: str) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=valid_url),
          mock.patch("app.main.has_internet_connection",
                     return_value=has_internet_connection)):
        assert expected_output == can_access_google_page("https://www.ez.com")
