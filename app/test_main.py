import pytest

from unittest import mock

from unittest.mock import MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_url: MagicMock,
        mocked_internet_connection: MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    mocked_url.return_value = valid_google_url
    mocked_internet_connection.return_value = has_internet_connection
    result = can_access_google_page("url")
    assert result == expected
