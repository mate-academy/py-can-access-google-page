import pytest
from unittest import mock

import app.main


@pytest.mark.parametrize(
    "google_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        google_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_url,
          mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):
        mocked_valid_url.return_value = google_url
        mocked_has_internet_connection.return_value = internet_connection

        result = app.main.can_access_google_page("https://www.google.com/")

        assert result == expected_result
