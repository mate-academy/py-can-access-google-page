from typing import Any
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "check_url, connection, access_to_google",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: Any,
        mocked_internet: Any,
        check_url: bool,
        connection: bool,
        access_to_google: str,
) -> None:
    mocked_url.return_value = check_url
    mocked_internet.return_value = connection

    assert can_access_google_page("google.com") == access_to_google
