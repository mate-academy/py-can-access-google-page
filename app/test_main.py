from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize("internet_connection, url, expected", [
    (True, True, "Accessible"),
    (False, False, "Not accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
])
def test_can_access_google_page(
        internet_connection: bool,
        url: bool,
        expected: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_connection,
        mock.patch("app.main.valid_google_url") as valid_url
    ):
        valid_connection.return_value = internet_connection
        valid_url.return_value = url
        assert can_access_google_page(
            "https://www.google.com/"
        ) == expected
