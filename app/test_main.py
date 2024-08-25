import pytest
from unittest.mock import patch
from app.main import can_access_google_page

URL = "http://example?"
NOT_ACCESSIBLE = "Not accessible"


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as has_internet_connection:
        yield has_internet_connection


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as valid_google_url:
        yield valid_google_url


def test_should_return_accessible_when_valid_url_and_connection_true(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(URL) == "Accessible"


def test_should_return_not_accessible_when_not_valid_url(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    assert can_access_google_page(URL) == NOT_ACCESSIBLE


def test_should_return_not_accessible_when_connection_false(
        mocked_has_internet_connection: str,
        mocked_valid_google_url: str
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page(URL) == NOT_ACCESSIBLE
