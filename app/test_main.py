from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_connected,is_valid_url,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "With connection and valid url you can access",
        "You can't access without connection",
        "You can't access with invalid url",
        "You can't access without connection with invalid url"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    connection: mock,
    correct_url: mock,
    is_connected: bool,
    is_valid_url: bool,
    expected: str
) -> None:
    connection.return_value = is_connected
    correct_url.return_value = is_valid_url

    assert can_access_google_page("url") == expected
