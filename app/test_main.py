from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "valid_url, connection, excepted_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_two_funktion(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        valid_url: bool,
        connection: bool,
        excepted_result: str,
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page("http://google.com") == excepted_result
