# write your code here
from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


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
def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_internet_connection: Mock,
        response: bool,
        current_time: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = response
    mock_internet_connection.return_value = current_time
    url = "https://www.google.com"
    assert can_access_google_page(url=url) == expected_result
