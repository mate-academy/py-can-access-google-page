from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, expected_url, connection, expected_result",
    [
        pytest.param("https://www.google.com/", True, False, "Not accessible"),
        pytest.param("https://www.google.com/", False, True, "Not accessible"),
        pytest.param("https://www.google.com/", True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: Callable,
                                mocked_has_internet_connection: Callable,
                                url: str,
                                expected_url: bool,
                                connection: bool,
                                expected_result: str) -> None:
    mocked_valid_google_url.return_value = expected_url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page(url) == expected_result
