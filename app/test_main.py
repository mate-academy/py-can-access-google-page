from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, access_google_page",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mocked_has_internet_connection: bool,
        mocked_valid_google_url: bool,
        has_internet_connection: bool,
        valid_google_url: bool,
        access_google_page: str
) -> None:
    mocked_has_internet_connection.return_value = has_internet_connection
    mocked_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("example_of_url") == access_google_page
