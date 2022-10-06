import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_url_and_connection_is_worked(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_valur = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_url_is_do_not_worked(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_valur = True
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_connection_is_not_worked(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"


def test_connection_and_url_is_not_worked(
    mocked_valid_google_url: None,
    mocked_has_internet_connection: None
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_valur = False
    assert can_access_google_page("https://www.google.com/") == "Not accessible"
