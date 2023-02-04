from app.main import can_access_google_page
from unittest import mock
import pytest

url = "https://www.google.com/"


@pytest.fixture()
def mocked_has_internet() -> mock:
    with mock.patch("app.main.has_internet_connection") as mocked_has_internet:
        yield mocked_has_internet


@pytest.fixture()
def mocked_valid_url() -> mock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


def test_should_call_has_internet_and_valid_url(
    mocked_has_internet: mock,
    mocked_valid_url: mock
) -> None:
    mocked_has_internet.return_value = True
    mocked_valid_url.return_value = True

    can_access_google_page(url)

    mocked_has_internet.assert_called_once()
    mocked_valid_url.assert_called_once_with(url)


def test_returns_accessible_when_both_checks_are_true(
    mocked_has_internet: mock,
    mocked_valid_url: mock
) -> None:
    mocked_has_internet.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page(url) == "Accessible"


def test_returns_not_accessible_when_no_internet(
    mocked_has_internet: mock,
    mocked_valid_url: mock
) -> None:
    mocked_has_internet.return_value = False
    mocked_valid_url.return_value = True

    assert can_access_google_page(url) == "Not accessible"


def test_returns_not_accessible_when_not_valid_url(
    mocked_has_internet: mock,
    mocked_valid_url: mock
) -> None:
    mocked_has_internet.return_value = True
    mocked_valid_url.return_value = False

    assert can_access_google_page(url) == "Not accessible"
