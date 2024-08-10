from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url",
    [
        "http://google.com",
        "http://abra_cadabra"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_has_called(
        mocked_has_connection: Mock,
        mocked_valid_url: Mock,
        url: str
) -> None:
    can_access_google_page(url)
    mocked_valid_url.assert_called_once_with(url)
    mocked_has_connection.assert_called_once()
