import pytest
from unittest import mock

import requests

from app.main import can_access_google_page, valid_google_url, has_internet_connection


@pytest.mark.parametrize(
    "url, time, expected",
    [
        ("https://www.google.com", 23, "Accessible"),
        ("https://www.google.com", 2, "Not accessible"),
        ("https://www.invalidurl.com", 10, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: mock.Mock,
        mocked_valid_google_url: mock.Mock,
        url: str,
        time: int,
        expected: str
) -> None:

    url_validation = True
    try:
        valid_google_url(url)
    except requests.exceptions.ConnectionError:
        url_validation = False
    mocked_valid_google_url.return_value = url_validation

    time_validation = True if time in range(6, 24) else False
    mocked_has_internet_connection.return_value = time_validation

    result = can_access_google_page(url)

    assert result == expected


@mock.patch("app.main.has_internet_connection")
def test_valid_google_url_called_once(
        mocked_has_internet_connection: mock.MagicMock,
) -> None:

    can_access_google_page("https://www.google.com/")
    mocked_has_internet_connection.assert_called_once()
