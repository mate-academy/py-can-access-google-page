from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_connection, result",
    [pytest.param(True, True, "Accessible", id="the page is available"),
     pytest.param(False, True, "Not accessible", id="not valid url"),
     pytest.param(True, False, "Not accessible", id="connection is lost")])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_google_url,
                                mocked_has_internet_connection,
                                is_valid_url, has_connection, result):
    mocked_valid_google_url.return_value = is_valid_url
    mocked_has_internet_connection.return_value = has_connection

    assert can_access_google_page("google.com") == result
