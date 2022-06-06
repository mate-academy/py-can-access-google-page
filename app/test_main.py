from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "response, time_now, result_msg",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Normal work"
        ),

        pytest.param(
            False,
            True,
            "Not accessible",
            id="Bad work, google url is not valid"
        ),

        pytest.param(
            True,
            False,
            "Not accessible",
            id="Bad work, internet connection is not available"
        ),

        pytest.param(
            False,
            False,
            "Not accessible",
            id="Bad work, google url is not valid "
               "and internet connection is not available"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        valid_url,
        connection_time,
        response,
        time_now,
        result_msg):

    valid_url.return_value = response
    connection_time.return_value = time_now

    assert can_access_google_page("url") == result_msg
