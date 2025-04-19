from urllib.error import URLError

import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "value_valid_google_url, value_has_internet_connection , result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.Mock,
        mock_valid_google_url: mock.Mock,
        value_valid_google_url: bool,
        value_has_internet_connection: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = value_has_internet_connection
    mock_valid_google_url.return_value = value_valid_google_url
    assert can_access_google_page("https://www.google.com") == result
