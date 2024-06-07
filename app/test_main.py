from app.main import can_access_google_page

import pytest

from unittest import mock


@pytest.mark.parametrize(
    "valid_url, has_internet_connection, expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "Test with correct params: Valid_url and Has_internet_connection",
        "Test with not correct has_internet_connection",
        "Test with not correct valid_url"
    ]
)
def test_can_access_google_page(valid_url: bool,
                                has_internet_connection: bool,
                                expected_value: str) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection") as mocked_int_connection
    ):
        mocked_url.return_value = valid_url
        mocked_int_connection.return_value = has_internet_connection

        assert can_access_google_page("url") == expected_value
