from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,is_connected,expected_response",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Valid URL, is connected",
        "Valid URL, no connection",
        "Invalid URL, is connected",
        "Invalid URL, no connection"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock,
        mocked_has_internet: mock,
        is_valid_url: bool,
        is_connected: bool,
        expected_response: str
) -> None:
    mocked_valid_url.return_value = is_valid_url
    mocked_has_internet.return_value = is_connected
    assert can_access_google_page("google.com") == expected_response
