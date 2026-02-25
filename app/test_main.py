from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        valid_url,
        has_connection,
        expected
):
    with mock.patch("app.main.valid_google_url") as mocked_url:
        with mock.patch("app.main.has_internet_connection") as mocked_conn:
            mocked_url.return_value = valid_url
            mocked_conn.return_value = has_connection

            result = can_access_google_page("https://www.google.com")

            assert result == expected
