from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_connection, mock_url, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_valid_url_and_connection(
        mock_connection: bool,
        mock_url: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url")
          as valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as has_internet_connection):
        has_internet_connection.return_value = mock_connection
        valid_google_url.return_value = mock_url
        assert can_access_google_page("google.com") == result
