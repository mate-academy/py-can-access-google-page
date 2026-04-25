from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
def test_can_access_google_page(
    internet_connection: bool,
    valid_url: bool,
    expected_result: str,
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet.return_value = internet_connection
        mock_valid_url.return_value = valid_url
        url = "https://www.google.com"
        assert can_access_google_page(url) == expected_result
