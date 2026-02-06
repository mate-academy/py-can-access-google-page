from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mocked_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_url_is_valid_and_connection_exist(mocked_valid_url, mocked_connection):
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("test") == "Accessible"


def test_url_is_valid_and_connection_not_exist(mocked_valid_url, mocked_connection):
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("test") == "Not accessible"


def test_url_is_not_valid(mocked_valid_url, mocked_connection):
    mocked_valid_url.return_value = False
    assert can_access_google_page("test") == "Not accessible"


def test_can_access_google_page_with_no_string_value() -> None:
    with pytest.raises(TypeError): can_access_google_page(123)
