from unittest import mock

import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,url_connection,result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should work normal"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessibly when site don't exist"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="haven't connection when time is out"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_to_google_page(
    mocked_has_internet_connection,
    mocked_valid_url,
    internet_connection,
    url_connection,
    result,
):
    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_url.return_value = url_connection

    assert can_access_google_page("google.com") == result
