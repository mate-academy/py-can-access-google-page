import pytest

from unittest import mock
from app.main import can_access_google_page
from typing import Callable


@pytest.fixture()
def mocked_valid_url() -> None:
    with (
        mock.patch("app.main.valid_google_url")
            as mock_valid_google_url
    ):
        yield mock_valid_google_url


@pytest.fixture()
def mocked_has_connection() -> None:
    with (
        mock.patch("app.main.has_internet_connection")
            as mock_has_connection
    ):
        yield mock_has_connection


@pytest.mark.parametrize(
    "is_valid_url,has_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        is_valid_url: bool,
        has_connection: bool,
        result: str,
        mocked_valid_url: Callable,
        mocked_has_connection: Callable,
) -> None:
    mocked_valid_url.return_value = is_valid_url
    mocked_has_connection.return_value = has_connection

    assert can_access_google_page("https://www.google.com/") == result
