from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_valid:
        yield mock_valid


@pytest.fixture()
def mocked_has_internet_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_true_true(mocked_valid_google_url: mock.MagicMock,
                   mocked_has_internet_connection: mock.MagicMock) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("google.com") == "Accessible"


def test_true_false(mocked_valid_google_url: mock.MagicMock,
                    mocked_has_internet_connection: mock.MagicMock) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"


def test_false_true(mocked_valid_google_url: mock.MagicMock,
                    mocked_has_internet_connection: mock.MagicMock) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page("google.com") == "Not accessible"


def test_false_false(mocked_valid_google_url: mock.MagicMock,
                     mocked_has_internet_connection: mock.MagicMock) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("google.com") == "Not accessible"
