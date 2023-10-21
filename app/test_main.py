import pytest
from unittest import mock

import requests

from app.main import valid_google_url, has_internet_connection, can_access_google_page


@pytest.mark.parametrize(
    "url_validation, connection_status, is_accessible",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        url_validation: bool,
        connection_status: bool,
        is_accessible: str
) -> None:
    mocked_valid_google_url.return_value = url_validation
    mocked_has_internet_connection.return_value = connection_status
    assert can_access_google_page("https://www.google.com") == is_accessible
