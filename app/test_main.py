from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def valid_google_url_mock() -> MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mock_has_internet() -> MagicMock:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_connection):
        yield mocked_has_connection


def test_can_access_google_page(
        valid_google_url_mock: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    valid_google_url_mock.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("") == "Accessible"


def test_return_not_accessible_if_no_internet_connection(
        valid_google_url_mock: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    valid_google_url_mock.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("") == "Not accessible"


def test_return_not_accessible_if_invalid_url(
        valid_google_url_mock: MagicMock,
        mock_has_internet: MagicMock
) -> None:
    valid_google_url_mock.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("") == "Not accessible"
