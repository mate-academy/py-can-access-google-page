# write your code here
from unittest import mock

import pytest

from app.main import can_access_google_page, valid_google_url, has_internet_connection


@pytest.mark.parametrize(
    "response, current_time, expected_result",
    [
        (
            True, True, "Accessible"
        ),
        (
            False, True, "Not accessible",
        ),
        (
            False, False, "Not accessible",
        ),
        (
            True, False, "Not accessible"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url, mock_internet_connection, response, current_time,
                                expected_result):
    mock_valid_google_url.return_value = response
    mock_internet_connection.return_value = current_time
    assert can_access_google_page(url="https://www.google.com") == expected_result
