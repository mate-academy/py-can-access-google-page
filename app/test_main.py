from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,is_connection,expected_access",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
        is_valid: bool,
        is_connection: bool,
        expected_access: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as has_connection,
          mock.patch("app.main.valid_google_url") as valid_url):
        has_connection.return_value = is_connection
        valid_url.return_value = is_valid
        assert can_access_google_page("url") == expected_access
