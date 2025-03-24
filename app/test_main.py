import pytest

from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url, connection, message",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Google accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Wrong url"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="No connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Wrong url and no connection"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_check_access(mocked_url, mocked_connection, url, connection, message):
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    assert can_access_google_page("www.google.com") == message
