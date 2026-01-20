from unittest import mock
import pytest

from .main import can_access_google_page


@pytest.fixture()
def mock_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as s:
        yield s


@pytest.fixture()
def mock_url() -> None:
    with mock.patch("app.main.valid_google_url") as s2:
        yield s2


def test_no_connection(mock_connection: any, mock_url: any) -> None:
    mock_connection.return_value = False
    mock_url.return_value = True

    assert can_access_google_page("") == "Not accessible"


def test_invalid_url(mock_connection: any, mock_url: any) -> None:
    mock_connection.return_value = True
    mock_url.return_value = False

    assert can_access_google_page("") == "Not accessible"


def test_all_correct(mock_connection: any, mock_url: any) -> None:
    mock_connection.return_value = True
    mock_url.return_value = True

    assert can_access_google_page("") == "Accessible"