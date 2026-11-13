from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "connection and valid url",
        "connection but invalid url",
        "valid url but no connection",
        "no connection and invalid url",
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


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_url_is_passed_to_valid_google_url(
    mocked_connection: mock.MagicMock,
    mocked_valid_url: mock.MagicMock,
) -> None:
    url = "https://www.google.com"
    can_access_google_page(url)
    mocked_valid_url.assert_called_once_with(url)
