from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_is_valid, connection_ok, result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Should be accessible"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Should not be accessible"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Should not be accessible"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_correct_action_advice(
        mocked_url_checker,
        mocked_conn_checker,
        url_is_valid,
        connection_ok,
        result
):
    mocked_url_checker.return_value = url_is_valid
    mocked_conn_checker.return_value = connection_ok
    assert can_access_google_page("mate.ua") == result
