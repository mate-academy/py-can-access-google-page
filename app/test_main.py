from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "is_valid_url,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mocked_valid_url: mock.MagicMock,
    mocked_connection: mock.MagicMock,
    is_valid_url: bool,
    has_connection: bool,
    expected: str,
) -> None:
    mocked_valid_url.return_value = is_valid_url
    mocked_connection.return_value = has_connection
    url = "https://www.google.com"
    assert main.can_access_google_page(url) == expected
