from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture
def mocked_valid_url() -> None:
    with (mock.patch("app.main.valid_google_url") as
          mock_test_valid_url):
        yield mock_test_valid_url


@pytest.fixture
def mocked_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection") as
          mock_test_internet_connection):
        yield mock_test_internet_connection


def test_can_access_google_with_valid_url_and_connection(
        mocked_valid_url: mock,
        mocked_internet_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Accessible"


def test_can_access_google_with_invalid_url_and_connection(
        mocked_valid_url: mock,
        mocked_internet_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = True
    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_access_google_with_valid_url_no_connection(
        mocked_valid_url: mock,
        mocked_internet_connection: mock
) -> None:
    mocked_valid_url.return_value = True
    mocked_internet_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"


def test_can_access_google_with_invalid_url_and_no_connection(
        mocked_valid_url: mock,
        mocked_internet_connection: mock
) -> None:
    mocked_valid_url.return_value = False
    mocked_internet_connection.return_value = False
    assert can_access_google_page("http://www.google.com") == "Not accessible"
