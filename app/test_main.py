from unittest import mock

import pytest

from app.main import can_access_google_page

@pytest.fixture
def mocked_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture
def mocked_internet():
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        yield mocked_internet


def test_can_access_google_page_when_valid_url(mocked_url, mocked_internet) -> None:
    mocked_url.return_value = True
    mocked_url.return_value = True

    result = can_access_google_page("https://www.google.com/")

    mocked_url.assert_called_with("https://www.google.com/")
    mocked_internet.assert_called_once()
    assert result == "Accessible"


def test_can_access_google_page_when_fake_url(mocked_url, mocked_internet) -> None:
    mocked_url.return_value = False
    mocked_internet.return_value = True

    result = can_access_google_page("fake_url")

    mocked_url.assert_called_with("fake_url")
    mocked_internet.assert_called_once()
    assert result == "Not accessible"