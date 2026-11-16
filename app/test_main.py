from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_url() -> any:
    with mock.patch("app.main.valid_google_url") as mock_test_url:
        mock_test_url.return_value = True
        yield mock_test_url


@pytest.fixture()
def mocked_has_internet() -> any:
    with (
        mock.patch("app.main.has_internet_connection") as mock_test_connection
    ):
        mock_test_connection.return_value = True
        yield mock_test_connection


def test_returns_accessible_when_internet_and_url_are_valid(
        mocked_has_internet: bool,
        mocked_valid_url: bool
) -> None:
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_returns_not_accessible_when_url_is_invalid(
        mocked_has_internet: bool,
        mocked_valid_url: bool
) -> None:
    mocked_valid_url.return_value = False
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


def test_returns_not_accessible_when_internet_is_unavailable(
        mocked_has_internet: bool,
        mocked_valid_url: bool
) -> None:
    mocked_has_internet.return_value = False
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


def test_returns_not_accessible_when_internet_and_url_are_invalid(
        mocked_has_internet: bool,
        mocked_valid_url: bool
) -> None:
    mocked_valid_url.return_value = False
    mocked_has_internet.return_value = False
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )
