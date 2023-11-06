# write your code here
import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, access",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="url valid and there is connection"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="url valid, but there is no connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="url isn't valid, but this is connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="url isn't valid and there is no connection"
        )
    ],
)
def test_can_access_google_page(
        valid_url: bool,
        internet_connection: bool,
        access: bool
) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_url,
          mock.patch("app.main.has_internet_connection") as mocked_connection):
        mocked_url.return_value = valid_url
        mocked_connection.return_value = internet_connection
        assert can_access_google_page("https://www.google.com/") == access
