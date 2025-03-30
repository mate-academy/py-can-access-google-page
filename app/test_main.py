import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_url.return_value = True
        yield mocked_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_internet:
        mocked_internet.return_value = True
        yield mocked_internet


def test_can_access_google_page(
    mocked_valid_google_url: mock,
    mocked_has_internet_connection: mock
) -> None:
    test = can_access_google_page("google.com")
    assert test == "Accessible"
    mocked_valid_google_url.assert_called_once_with("google.com")
    mocked_has_internet_connection.assert_called_once()


def test_no_access_google_page_invalid_url(
    mocked_valid_google_url: mock,
    mocked_has_internet_connection: mock
) -> None:
    mocked_valid_google_url.return_value = False
    test = can_access_google_page("test123")
    assert test == "Not accessible"
    mocked_valid_google_url.assert_called_once_with("test123")
    mocked_has_internet_connection.assert_called_once()


def test_no_access_google_page_no_internet(
    mocked_valid_google_url: mock,
    mocked_has_internet_connection: mock
) -> None:
    mocked_has_internet_connection.return_value = False
    test = can_access_google_page("google.com")
    assert test == "Not accessible"
    mocked_has_internet_connection.assert_called_once()
