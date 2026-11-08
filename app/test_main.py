from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid url and connection give access",
        "valid url without connection gives no access",
        "connection with invalid url gives no access",
        "no valid url and no connection give no access",
    ]
)
def test_access_depends_on_valid_url_and_connection(
        is_valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=is_valid_url),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=has_connection
        ),
    ):
        assert can_access_google_page("https://www.google.com") == expected
