import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, valid, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        connection: bool, valid: bool, expected: str) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        with mock.patch("app.main.valid_google_url") as mocked_valid:
            mocked_connection.return_value = connection
            mocked_valid.return_value = valid
            assert can_access_google_page("https://www.google.com") == expected
