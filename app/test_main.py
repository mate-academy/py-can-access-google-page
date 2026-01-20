from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, url, result",
    [
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Invalid URL"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not internet time"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Valid url and correct time"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url,
        mocked_has_internet_connection,
        internet_connection,
        url,
        result
):
    mocked_valid_google_url.return_value = url
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("google.com") == result
