import pytest
from unittest import mock


@pytest.fixture()
def mocking_valid_google_url():
    with mock.patch("valid_google_url") as func:
        yield func


@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("has_internet_connection") as func:
            yield func


def test_can_access_google_page(mocking_valid_google_url, mocked_has_internet_connection) -> None:
    mocking_valid_google_url.assert_called_once()
    mocked_has_internet_connection.assert_called()