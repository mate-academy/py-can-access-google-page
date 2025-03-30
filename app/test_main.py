from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_is_valid, connection_is_valid, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid_url_and_connection",
        "valid_url_invalid_connection",
        "invalid_url_valid_connection",
        "invalid_url_and_connection"
    ]
)
def test_can_access_to_page(
        url_is_valid: bool,
        connection_is_valid: bool,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_url,
        mock.patch("app.main.has_internet_connection") as mock_connection
    ):
        mock_url.return_value = url_is_valid
        mock_connection.return_value = connection_is_valid
        assert can_access_google_page("https://google.com") == expected_result
