from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection_value,valid_google_url_value,result",
    [
        (
            True,
            True,
            "Accessible"
        ),
        (
            True,
            False,
            "Not accessible"
        ),
        (
            False,
            True,
            "Not accessible"
        ),
        (
            False,
            False,
            "Not accessible"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def tester(valid_google_url: mock,
           has_internet_connection: mock,
           has_internet_connection_value: bool,
           valid_google_url_value: bool,
           result: str) -> None:
    has_internet_connection.return_value = has_internet_connection_value
    valid_google_url.return_value = valid_google_url_value
    assert can_access_google_page("https://www.google.com/") == result
