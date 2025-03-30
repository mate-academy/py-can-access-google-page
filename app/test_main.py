from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
def test_connection_and_url(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page("https://www.google.com.ua/")
    assert result == expected_result
