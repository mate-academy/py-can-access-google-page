from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_has_internet_connection: mock.MagicMock,
    mocked_valid_google_url: mock.MagicMock,
    has_internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mocked_has_internet_connection.return_value = has_internet
    mocked_valid_google_url.return_value = valid_url

    url = "https://www.google.com"
    assert can_access_google_page(url) == expected

    mocked_has_internet_connection.assert_called_once()
    if has_internet:
        mocked_valid_google_url.assert_called_once_with(url)
    else:
        mocked_valid_google_url.assert_not_called()
