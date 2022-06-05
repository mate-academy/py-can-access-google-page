import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "testing_connection,testing_url,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="have access and valid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="no internet connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="not valid url"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_access(
        is_connected_func,
        is_url_exist_func,
        testing_connection,
        testing_url,
        expected):
    is_connected_func.return_value = testing_connection
    is_url_exist_func.return_value = testing_url
    assert can_access_google_page("google.com") == expected
