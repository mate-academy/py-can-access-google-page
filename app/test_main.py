import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, url, expected_result", [
        pytest.param(
            True, True, "Accessible"
        ),

        pytest.param(
            True, False, "Not accessible"
        ),

        pytest.param(
            False, False, "Not accessible"
        ),

        pytest.param(
            False, True, "Not accessible"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_get_access(
        mocked_connection,
        mocked_valid,
        connection,
        url,
        expected_result
):
    mocked_valid.return_value = url
    mocked_connection.return_value = connection

    assert can_access_google_page("https://www.google.com") == expected_result
