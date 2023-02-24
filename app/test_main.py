import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_validation_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_site() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_valid_url_and_connection(
        mocked_validation_url: mock,
        mocked_site: mock
) -> None:
    mocked_validation_url.return_value = True
    mocked_site.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_valid_url(
        mocked_validation_url: mock,
        mocked_site: mock
) -> None:
    mocked_validation_url.return_value = False
    mocked_site.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_no_connection(
        mocked_validation_url: mock,
        mocked_site: mock
) -> None:
    mocked_validation_url.return_value = True
    mocked_site.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_valid_connection_and_url(
        mocked_validation_url: mock,
        mocked_site: mock
) -> None:
    mocked_validation_url.return_value = False
    mocked_site.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
