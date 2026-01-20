import pytest

from app.main import can_access_google_page
from typing import Callable
from unittest import mock


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


class TestCorrectlyWork:
    @pytest.mark.parametrize(
        "connection,valid_url,answer",
        [
            (
                True,
                False,
                "Not accessible"
            ),
            (
                False,
                True,
                "Not accessible"
            ),
            (
                True,
                True,
                "Accessible"
            ),
            (
                False,
                False,
                "Not accessible"
            )
        ]
    )
    def test_function_work_correctly(
        self,
        connection: bool,
        valid_url: bool,
        answer: str,
        mocked_has_internet_connection: Callable,
        mocked_valid_google_url: Callable
    ) -> None:
        mocked_has_internet_connection.return_value = connection
        mocked_valid_google_url.return_value = valid_url
        assert can_access_google_page(
            "http://www.google.com/intl/uk/privacy"
        ) == answer
