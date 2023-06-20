from unittest import mock
import pytest

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "has_internet, is_valid, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        valid_google_url: mock.MagicMock,
        has_internet_connection: mock.MagicMock,
        has_internet: bool,
        is_valid: bool,
        expected: str,

) -> None:
    has_internet_connection.return_value = has_internet
    valid_google_url.return_value = is_valid
    assert can_access_google_page("dummy url") == expected
