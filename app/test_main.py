from unittest import mock

import pytest

from app.main import can_access_google_page

test_url = "test_url"


@pytest.mark.parametrize(
    "valid_google_url_return_value, "
    "has_internet_connection_return_value, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock,
        valid_google_url_return_value: bool,
        has_internet_connection_return_value: bool,
        result: str) -> None:
    mocked_valid_google_url.return_value = valid_google_url_return_value
    mocked_has_internet_connection.return_value = (
        has_internet_connection_return_value)
    assert can_access_google_page(test_url) == result
