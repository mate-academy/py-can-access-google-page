from unittest import mock
from typing import Any

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_google_url:
        yield mocked_google_url


@pytest.fixture
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "google_url, internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid url and connection",
        "not valid connection",
        "not valid url",
        "both not valid",
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any,
        google_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = google_url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com/") == result
