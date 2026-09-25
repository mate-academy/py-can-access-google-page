from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid url and connection exists",
        "invalid url with connection",
        "valid url without connection",
        "invalid url without connection",
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_connection: mock.MagicMock,
    mocked_valid_url: mock.MagicMock,
    has_connection: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    mocked_connection.return_value = has_connection
    mocked_valid_url.return_value = is_valid_url

    assert can_access_google_page("https://www.google.com") == expected
