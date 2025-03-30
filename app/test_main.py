import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,expected_res",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        has_connection: bool,
        expected_res: str
) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection, \
         mock.patch("app.main.valid_google_url") as mocked_valid:
        mocked_connection.return_value = has_connection
        mocked_valid.return_value = valid_url
        assert can_access_google_page("https://www.google.com") == expected_res
