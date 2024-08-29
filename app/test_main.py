from unittest import mock

import pytest

from app.main import (can_access_google_page)


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access(has_internet_func: bool, valid_google_func: str,
                internet_connection: bool, valid_url: bool,
                result: str) -> None:
    has_internet_func.return_value = internet_connection
    valid_google_func.return_value = valid_url
    assert can_access_google_page(valid_google_func) == result
