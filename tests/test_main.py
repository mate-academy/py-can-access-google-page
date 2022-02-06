from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid,has_connection,expected_advice",
    [
        (
            True,
            True,
            "Accessible"
        ),
        (
            True,
            False,
            "Not accessible"
        ),
        (
            False,
            True,
            "Not accessible"
        ),
(
            False,
            False,
            "Not accessible"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google(
                        mocked_request,
                        mocked_connection,
                        is_valid,
                        has_connection,
                        expected_advice
                    ):
    mocked_request.return_value = is_valid
    mocked_connection.return_value = has_connection

    assert can_access_google_page("http://www.google.com") == expected_advice
