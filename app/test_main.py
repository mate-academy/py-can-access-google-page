import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, status_internet_connection, result",
    [
        pytest.param(False, False, "Not accessible",
                     id="No internet and urs is uncorrected"),
        pytest.param(False, True, "Not accessible",
                     id="Don`t valid_url"),
        pytest.param(True, False, "Not accessible",
                     id="Hasn`t internet"),
        pytest.param(True, True, "Accessible",
                     id="Access connection")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_func_internet_connect,
        mocked_valid_url,
        status_internet_connection,
        valid_url,
        result
):
    mocked_valid_url.return_value = valid_url
    mocked_func_internet_connect.return_value = status_internet_connection

    assert can_access_google_page("google.com") == result
