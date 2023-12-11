from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "valid url and has internet connection",
        "valid url and hasn't internet connection",
        "invalid url and has internet connection",
        "invalid url and hasn't internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_validator: callable,
        mocked_internet: callable,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    mocked_validator.return_value = valid_url
    mocked_internet.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
