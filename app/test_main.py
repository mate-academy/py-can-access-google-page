from unittest import mock
import app.main
import pytest


@pytest.mark.parametrize("url, internet_connection, expected", [
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (True, True, "Accessible"),
    (False, False, "Not accessible")
])
def test_can_access_google_page(
        url: str,
        internet_connection: None,
        expected: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
         mock.patch("app.main.has_internet_connection")
         as mocked_has_internet_connection):

        mocked_valid_google_url.return_value = url
        mocked_has_internet_connection.return_value = internet_connection

        result = app.main.can_access_google_page("http://www.google.com")

        assert result == expected
