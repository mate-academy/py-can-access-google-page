from unittest import mock
import pytest


from app.main import can_access_google_page


@pytest.fixture()
def mocked_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mocked_internet() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_time:
        yield mocked_time


def test_can_access_google_page_with_internet_and_valid_url(
        mocked_url: mock.MagicMock,
        mocked_internet: mock.MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_with_internet_and_invalid_url(
        mocked_url: mock.MagicMock,
        mocked_internet: mock.MagicMock
) -> None:
    mocked_internet.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_with_no_internet_and_valid_url(
        mocked_url: mock.MagicMock,
        mocked_internet: mock.MagicMock
) -> None:
    mocked_internet.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"
