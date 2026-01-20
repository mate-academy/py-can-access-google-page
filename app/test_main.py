from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url_valid: bool,
        internet_connection: bool,
        expected: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as valid_google_url,
          mock.patch(
              "app.main.has_internet_connection") as has_internet_connection
          ):
        has_internet_connection.return_value = internet_connection
        valid_google_url.return_value = url_valid
        assert can_access_google_page("https://www.dckids.com/") == expected
