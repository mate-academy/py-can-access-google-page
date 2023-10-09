import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "validation_result, internet_connection_result, access_to_page",
    [
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Close access without internet connection and valid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Close access without valid url"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Close access without internet connection"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Access with internet connection and valid url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_check_access_google_page(
    mocked_valid_google_url: callable,
    mocked_internet_connection: callable,
    validation_result: bool,
    internet_connection_result: bool,
    access_to_page: str
) -> None:
    mocked_valid_google_url.return_value = validation_result
    mocked_internet_connection.return_value = internet_connection_result
    assert can_access_google_page("https://www.google.com/") == access_to_page
