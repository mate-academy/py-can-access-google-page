import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page_if_internet_connection_and_valid_url(
        valid_url: bool,
        internet_connection: bool,
        expected: str) -> None:
    with (mock.patch("app.main.valid_google_url") as mocked_valid_google_url,
          mock.patch("app.main.has_internet_connection") as
          mocked_has_internet_connection):
        mocked_valid_google_url.return_value = valid_url
        mocked_has_internet_connection.return_value = internet_connection
        assert (
            can_access_google_page("test_url") == expected
        )
