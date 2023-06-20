from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "mocked_connection, mocked_url, result",
        [
            (True, True, "Accessible"),

            (True, False, "Not accessible"),

            (False, True, "Not accessible"),

            (False, False, "Not accessible")
        ],
        ids=[
            "Page is accessible - stable connection and url is valid",
            "Page is NOT accessible - url is invalid",
            "Page is NOT accessible - no connection",
            "Page is NOT accessible - no connection and url is invalid"
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_can_access_google_page(
        self,
        has_internet_connection: Callable,
        valid_google_url: Callable,
        mocked_connection: bool,
        mocked_url: bool,
        result: str
    ) -> None:
        valid_google_url.return_value = mocked_url
        has_internet_connection.return_value = mocked_connection

        assert can_access_google_page("https://mate.academy/courses/python") == result
