from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        yield mocked_valid_google_url


@pytest.fixture()
def mock_has_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):
        yield mocked_has_internet_connection


def test_should_return_accessible_if_all_checks_are_valid(
        mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_you_cannot_access_page_if_only_connection_is_true(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


def test_you_cannot_access_page_if_only_valid_url_is_true(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
