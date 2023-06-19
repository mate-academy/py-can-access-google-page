from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "expected_url, connection, expected_result",
    [
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: Callable,
                                mocked_has_internet_connection: Callable,
                                expected_url: bool,
                                connection: bool,
                                expected_result: str) -> None:
    mocked_valid_google_url.return_value = expected_url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page("https://www.google.com") == expected_result
