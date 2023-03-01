from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected_result", [
    pytest.param(
        True, True, "Accessible",
        id="test_is_internet_valid_url"
    ),
    pytest.param(
        False, True, "Not accessible",
        id="test_is_internet_invalid_url"
    ),
    pytest.param(
        True, False, "Not accessible",
        id="test_no_internet_valid_url"
    ),
    pytest.param(
        False, False, "Not accessible",
        id="test_no_internet_invalid_url"
    ),
])
def test_can_access_google_page(
        valid_url: str,
        has_connection: bool,
        expected_result: str,
) -> None:
    with mock.patch(
            "app.main.valid_google_url", return_value=valid_url
    ), mock.patch(
        "app.main.has_internet_connection", return_value=has_connection
    ):
        assert can_access_google_page(
            "http://www.google.com"
        ) == expected_result
