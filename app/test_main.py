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
        mock_url: mock,
        mock_connection: mock
) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_valid_url(
        mock_url: mock,
        mock_connection: mock
) -> None:
    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_no_connection(
        mock_url: mock,
        mock_connection: mock
)-> None:
    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_valid_connection_and_url(
        mock_url: mock,
        mock_connection: mock
) -> None:
    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
