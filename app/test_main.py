from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected",
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
    mocked_internet: mock.MagicMock,
    is_valid_url: bool,
    has_internet: bool,
    expected: str,
) -> None:
    mocked_valid_url.return_value = is_valid_url
    mocked_internet.return_value = has_internet

    assert can_access_google_page("https://www.google.com") == expected
