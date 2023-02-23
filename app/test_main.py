import pytest
from unittest import mock

from app.main import can_access_google_page

use_case_data = [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
]

ids = [
    "get access when 'connection' and 'url' are valid",
    "denied access when current time not in range 6:00 - 22:00",
    "denied access when invalid 'url' was passed"
]


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "is_connected,is_valid,expected",
    use_case_data,
    ids=ids
)
def test_can_access_google_page(
        mocked_internet_connection: mock.MagicMock,
        mocked_valid_url: mock.MagicMock,
        is_connected: bool,
        is_valid: bool,
        expected: str
) -> None:
    mocked_internet_connection.return_value = is_connected
    mocked_valid_url.return_value = is_valid
    assert can_access_google_page("https://example.com/") == expected
