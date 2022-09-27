from app.main import can_access_google_page

from unittest import mock

import pytest


@pytest.fixture()
def mocked_internet():
    with mock.patch("app.main.has_internet_connection") as mock_func:
        yield mock_func


@pytest.fixture()
def mocked_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_func:
        yield mock_func


def test_return_accessible(mocked_internet, mocked_valid_url):
    mocked_internet.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page("") == "Accessible"


def test_return_not_accessible_if_internet_is_false(mocked_internet,
                                                    mocked_valid_url):
    mocked_internet.return_value = False
    mocked_valid_url.return_value = True

    assert can_access_google_page("") == "Not accessible"


def test_return_not_accessible_if_url_is_false(mocked_internet,
                                               mocked_valid_url):
    mocked_internet.return_value = True
    mocked_valid_url.return_value = False

    assert can_access_google_page("") == "Not accessible"
