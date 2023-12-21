from unittest.mock import patch

import pytest

from app.main import can_access_google_page


def test_valid_google_url() -> None:
    pass


def test_has_internet_connection() -> None:
    pass


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
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    mocked_has_internet_connection.return_value = valid_url
    mocked_valid_google_url.return_value = internet_connection
    assert (
        can_access_google_page("https://www.google.com/") == expected_result
    )
