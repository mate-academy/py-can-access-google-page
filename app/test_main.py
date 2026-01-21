import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "access granted",
        "not have connection",
        "not valid url",
        "not connection and valid url"
    ]
)
def test_valid_google_url(test_url: bool,
                          has_connection: bool,
                          expected: str
                          ) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_test_url, \
         mock.patch("app.main.has_internet_connection") as mocked_connection:
        mocked_test_url.return_value = test_url
        mocked_connection.return_value = has_connection

        assert can_access_google_page("https://google.com") == expected
