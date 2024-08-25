from unittest import mock
from typing import Any

from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "url,"
    "expected_value,"
    "mocked_return_value_valid_google_url,"
    "mocked_return_value_connection",
    [
        pytest.param(
            "https://www.google.com.ua/?hl=ukar",
            "Accessible",
            True,
            True,
            id="test can access google page return Accessible"
        ),
        pytest.param(
            "https://www.goosdofighoidjfggle.com.ua/?hl=uk",
            "Not accessible",
            False,
            True,
            id="test can access google page, "
               "valid google url return Not accessible"
        ),
        pytest.param(
            "https://www.goosdofighoidkjhihjfggle.com.ua/?hl=uk",
            "Not accessible",
            True,
            False,
            id="test can access google page, "
               "has internet connection "
               "return Not accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: Any,
        mocked_connection: Any,
        url: str,
        expected_value: str,
        mocked_return_value_valid_google_url: bool,
        mocked_return_value_connection: bool
) -> None:
    mocked_valid_google_url.return_value = mocked_return_value_valid_google_url
    mocked_connection.return_value = mocked_return_value_connection
    assert can_access_google_page(url) == expected_value
