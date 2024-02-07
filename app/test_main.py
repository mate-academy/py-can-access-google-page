import pytest
from unittest import mock
from app.main import can_access_google_page



@pytest.fixture
def get_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture
def get_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_can_access_google_page_true(
        get_valid_google_url: object,
        get_connection: object
) -> None:
    get_valid_google_url.return_value = True
    get_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_action_valid_url_false(
        get_valid_google_url: object,
        get_connection: object
) -> None:
    get_valid_google_url.return_value = False
    get_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_action_connection_false(
        get_valid_google_url: object,
        get_connection: object
) -> None:
    get_valid_google_url.return_value = True
    get_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
