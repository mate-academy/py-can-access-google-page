from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, result",
    [
        pytest.param(
            True,
            True,
            "Accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            False,
            False,
            "Not accessible"
        ),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url,
        mocked_connection,
        valid_url,
        internet_connection,
        result
):
    mocked_url.return_value = valid_url
    mocked_connection.return_value = internet_connection

    assert can_access_google_page("google.com") == result
