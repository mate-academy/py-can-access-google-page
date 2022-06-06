from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,url_connection,access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should have access"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Url should be in valid values"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Internet connection should be exists"
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
    access,
):
    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_url.return_value = url_connection

    assert can_access_google_page("google.com") == access
