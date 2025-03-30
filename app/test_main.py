from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expect",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],

    ids=["we can get access with url and connection valid",
         "we can't get access without connection",
         "we can't get access without valid url",
         "we can't get access without both"]
)
def test_can_access_google_page(valid_url: bool,
                                connection: bool,
                                expect: str,) -> None:
    with (mock.patch("app.main.valid_google_url")
          as valid_ur,
         (mock.patch("app.main.has_internet_connection"))
         as success_connection):
        valid_ur.return_value = valid_url
        success_connection.return_value = connection
        assert can_access_google_page("url") == expect
