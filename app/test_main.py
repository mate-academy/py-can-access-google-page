import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_url() -> callable:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_internet() -> callable:
    with mock.patch("app.main.has_internet_connection") \
            as mocked_internet:
        yield mocked_internet


def test_url_and_internet_exist(mock_url: callable,
                                mock_internet: callable) -> None:
    mock_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("url") == "Accessible"


def test_url_and_internet_dont_exist(mock_url: callable,
                                     mock_internet: callable) -> None:
    mock_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("url") == "Not accessible"


def test_url_dont_exist_internet_exist(mock_url: callable,
                                       mock_internet: callable) -> None:
    mock_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("url") == "Not accessible"


def test_url_exist_internet_dont_exist(mock_url: callable,
                                       mock_internet: callable) -> None:
    mock_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("url") == "Not accessible"
