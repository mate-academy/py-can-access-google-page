from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Internet connection is true, url is valid - Accessible",
        "Internet connection is true, url is not valid - Not accessible",
        "Internet connection is false, url is valid - Not accessible",
        "Internet connection is false, url is not valid - Not accessible",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        internet_connection: bool,
        valid_url: bool,
        expected: str
) -> None:
    url = "https://www.google.com/"

    can_access_google_page(url)
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with(url)

    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_google_url.return_value = valid_url

    assert can_access_google_page(url) == expected
