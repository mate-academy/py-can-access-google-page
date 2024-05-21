import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection,valid_google_url,expected_access",
    [
        pytest.param(
            True, False, "Not accessible",
            id="shouldn't work without internet connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="shouldn't work without valid url"
        ),
        pytest.param(
            True, True, "Accessible",
            id="should work with valid url and connection"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_check_internet_connection(
        mocked_internet_connection: bool,
        mocked_valid_google_url: bool,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_access: str
) -> None:
    mocked_internet_connection.return_value = has_internet_connection
    mocked_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("test_url") == expected_access
