from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "param1,param2,url,expected",
    [
        (True, True, "https//:www.google.com", "Accessible"),
        (False, True, "https//:www.google.com", "Not accessible"),
        (True, False, "https//:www.google.com", "Not accessible"),
        (False, False, "https//:www.google.com", "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_valid_url: object,
        mocked_has_connection: object,
        param1: bool,
        param2: bool,
        url: str,
        expected: str
) -> None:
    mocked_valid_url.return_value = param1
    mocked_has_connection.return_value = param2

    assert can_access_google_page(url) == expected
