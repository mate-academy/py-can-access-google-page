from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_internet_connection, expected_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "valid url and has connection - Accessible",
        "valid url and hasn't connection - Not accessible",
        "invalid url and has connection - Not accessible",
        "invalid url and hasn't connection - Not accessible",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock,
        mocked_has_internet: mock,
        is_valid_url: bool,
        is_internet_connection: bool,
        expected_access: str) -> None:
    mocked_valid_url.return_value = is_valid_url
    mocked_has_internet.return_value = is_internet_connection
    assert can_access_google_page("site") == expected_access
