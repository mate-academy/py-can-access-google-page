
# write your code here
from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "internet_connection, google_url, result",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_how_the_function_works(
        mocked_valid_url: bool,
        mocked_connection: bool,
        internet_connection: bool,
        google_url: bool,
        result: str
) -> None:
    mocked_connection.return_value = internet_connection
    mocked_valid_url.return_value = google_url
    assert can_access_google_page("") == result
