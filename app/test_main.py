from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "is_url_valid,is_have_internet,expected_result",
    [
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Should be not accessible if url isn't valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Should be not accessible if there is no internet connection"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should be accessible if pass all validators"
        ),
    ]
)
def test_valid_url_and_connection_exists(
        mocked_url_validator: Callable,
        mocked_internet_checker: Callable,
        is_url_valid: bool,
        is_have_internet: bool,
        expected_result: str) -> None:
    mocked_url_validator.return_value = is_url_valid
    mocked_internet_checker.return_value = is_have_internet
    assert can_access_google_page("google.com") == expected_result
