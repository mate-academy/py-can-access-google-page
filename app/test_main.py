from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize("valid_google_url, has_internet_connection, expected",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                             (False, False, "Not accessible"),
                         ]
                         )
def test_can_access_google_page(
        mocked_valid: str,
        mocked_connection: str,
        valid_google_url: str,
        has_internet_connection: str,
        expected: str,
) -> None:

    mocked_valid.return_value = valid_google_url
    mocked_connection.return_value = has_internet_connection

    assert can_access_google_page("url") == expected
