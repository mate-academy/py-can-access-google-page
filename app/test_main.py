from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result", [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible'",
        "Should return 'Not accessible', if function receive invalid url",
        "Should return 'Not accessible', if hasn't internet connection"
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection") as mocked_int_connection
    ):
        mocked_url.return_value = valid_url
        mocked_int_connection.return_value = internet_connection

        assert can_access_google_page("url") == expected_result
