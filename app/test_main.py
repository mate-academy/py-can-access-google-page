from unittest import mock
import pytest
from typing import Callable
from app.main import can_access_google_page


@pytest.fixture
def valid_google_url() -> None:
    with (
        mock.patch("app.main.valid_google_url")
        as mock_google_url
    ):
        yield mock_google_url


@pytest.fixture
def has_internet_connection() -> None:
    with (
        mock.patch("app.main.has_internet_connection")
        as mock_internet_connection
    ):
        yield mock_internet_connection


@pytest.mark.parametrize(
    "google_url,connection,return_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_google_url: Callable,
        has_internet_connection: Callable,
        google_url: bool,
        connection: bool,
        return_result: str
) -> None:
    valid_google_url.return_value = google_url
    has_internet_connection.return_value = connection

    assert can_access_google_page("") == return_result
