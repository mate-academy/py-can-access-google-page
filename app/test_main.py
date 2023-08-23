from unittest import mock

import pytest as pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_return_value,"
    "has_internet_return_value,"
    "expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should be accessible if url is valid, connection is true",
        "should NOT be accessible if url is valid, connection is false",
        "should NOT be accessible if url is not valid, connection is true",
        "should NOT be accessible if url is not valid, connection is false",
    ]
)
def test_can_access_google_page(
        valid_url_return_value: bool,
        has_internet_return_value: bool,
        expected_result: str
) -> None:

    with (
        mock.patch("app.main.valid_google_url") as mocked_valid_url,
        mock.patch("app.main.has_internet_connection") as mocked_has_internet
    ):
        mocked_valid_url.return_value = valid_url_return_value
        mocked_has_internet.return_value = has_internet_return_value

        actual_result = can_access_google_page("")

    assert actual_result == expected_result
