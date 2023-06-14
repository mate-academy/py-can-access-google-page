from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "connection_mock,url_mock,expected_result,url",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                "https://mate.academy/en/courses/python",
                id="accessible when user with connection and url is valid"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                "https://invalid.academy/en/courses/1)",
                id="Not accessible when url invalid"
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                "https://mate.academy/en/courses/python",
                id="Not accessible without internet connection"
            )
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_accessible_when_user_with_internet_and__url_is_valid(
            self,
            has_internet_connection: Callable,
            valid_google_url: Callable,
            connection_mock: bool,
            url_mock: bool,
            url: str,
            expected_result: str
    ) -> None:
        has_internet_connection.return_value = connection_mock
        valid_google_url.return_value = url_mock

        assert can_access_google_page(url) == expected_result
