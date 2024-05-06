from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,result",
    [
        pytest.param(True, True, "Accessible",
                     id="connection/url should be 'T'/'T'"),
        pytest.param(True, False, "Not accessible",
                     id="connection/url should be 'T'/'F'"),
        pytest.param(False, True, "Not accessible",
                     id="connection/url should be 'F'/'T'"),
        pytest.param(False, False, "Not accessible",
                     id="connection/url should be 'F'/'F'")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: bool,
        mocked_connection: bool,
        url: bool,
        connection: bool,
        result: str) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    assert can_access_google_page("https://www.google.com") == result
