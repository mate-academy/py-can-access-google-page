import unittest.mock
from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def has_connect() -> unittest.mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked_has_connect:
        yield mocked_has_connect


@pytest.fixture()
def valid_url() -> unittest.mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


def test_valid_url_and_connection_exists(has_connect: unittest.mock.MagicMock,
                                         valid_url: unittest.mock.MagicMock) \
        -> None:
    can_access_google_page("https://google.com")
    valid_url.assert_called_once_with("https://google.com")
    has_connect.assert_called_once()


@pytest.mark.parametrize(
    "is_valid_url, is_has_connect, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "google.com is exists and connection work",
        "google.com is exists and connection do not work",
        "google.com is not exists and connection work",
        "google.com is not exists and connection do not work"
    ]
)
def test_can_access_google(has_connect: unittest.mock.MagicMock,
                           valid_url: unittest.mock.MagicMock,
                           is_valid_url: bool, is_has_connect: bool,
                           result: str) -> None:
    has_connect.return_value = is_has_connect
    valid_url.return_value = is_valid_url
    assert can_access_google_page("https://google.com") == result
