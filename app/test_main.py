from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "check_google_url,check_has_internet_connection,expected_result",
    [pytest.param(
        True, True, "Accessible",
        id="valid url and internet connection exist"
    ), pytest.param(
        False, False, "Not accessible",
        id="not valid url and internet connection does not exist"
    ), pytest.param(
        True, False, "Not accessible",
        id="valid url but internet does not connection exist"
    ), pytest.param(
        False, True, "Not accessible",
        id="not valid url but internet connection exist"
    ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_url: bool,
        mocked_internet_connection: bool,
        check_google_url: bool,
        check_has_internet_connection: bool,
        expected_result: str
) -> None:
    mocked_url.return_value = check_google_url
    mocked_internet_connection.return_value = check_has_internet_connection

    assert can_access_google_page("google.com") == expected_result
