from unittest import mock
from typing import Any
import pytest

from app import main


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google_url):
        yield mock_valid_google_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection") as
          mock_has_internet_connection):
        yield mock_has_internet_connection


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: Any,
        mocked_has_internet_connection: Any,
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    assert main.can_access_google_page("") == result
