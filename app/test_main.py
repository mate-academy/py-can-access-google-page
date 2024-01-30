import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expect, ids",
    [
        (True, True, "Accessible", "we can get access"),
        (True, False, "Not accessible", "we can't get"
                                        " access without connection"),
        (False, True, "Not accessible", "we can't get"
                                        " access without valid url"),
        (False, False, "Not accessible", "we can't get"
                                         " access without both")
    ]
)
def test_can_access_google_page(valid_url: bool,
                                connection: bool,
                                expect: str,
                                ids: str) -> None:
    with (mock.patch("app.main.valid_google_url")
          as valid_ur,
         (mock.patch("app.main.has_internet_connection"))
         as success_connection):
        valid_ur.return_value = valid_url
        success_connection.return_value = connection
        assert can_access_google_page("url") == expect, ids
