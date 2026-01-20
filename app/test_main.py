from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access(
    mocked_google_url: mock,
    mocked_internet_connection: mock,
    valid_url: bool,
    connection: bool,
    expected_result: str
) -> None:
    mocked_google_url.return_value = valid_url
    mocked_internet_connection.return_value = connection
    result = can_access_google_page("https://www.google.com")
    assert result == expected_result
