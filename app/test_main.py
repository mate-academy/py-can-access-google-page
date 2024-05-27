from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url():
    with (mock.patch("app.main.valid_google_url")) as mock_valid:
        yield mock_valid


@pytest.fixture()
def mock_has_internet_connection():
    with (mock.patch("app.main.has_internet_connection")) as mock_connection:
        yield mock_connection


def test_can_access_google_page_accsesible(mock_valid_google_url, mock_has_internet_connection) -> None:
    # with (mock.patch("app.main.has_internet_connection")
    #       as mock_has_internet_connection,
    #       mock.patch("app.main.valid_google_url")
    #       as mock_valid_google_url):

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    can_access_google_page("Test")

    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("Test")

    assert can_access_google_page("") == "Accessible"


def test_can_access_google_page_not_accsesible_1_0(mock_valid_google_url, mock_has_internet_connection) -> None:
    # with (mock.patch("app.main.has_internet_connection")
    #       as mock_has_internet_connection,
    #       mock.patch("app.main.valid_google_url")
    #       as mock_valid_google_url):

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    can_access_google_page("")

    assert can_access_google_page("") == "Not accessible"


def test_can_access_google_page_not_accsesible_0_1(mock_valid_google_url, mock_has_internet_connection) -> None:
    # with (mock.patch("app.main.has_internet_connection")
    #       as mock_has_internet_connection,
    #       mock.patch("app.main.valid_google_url")
    #       as mock_valid_google_url):

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    can_access_google_page("")

    assert can_access_google_page("") == "Not accessible"


def test_can_access_google_page_not_accsesible_0(mock_valid_google_url, mock_has_internet_connection) -> None:
    # with (mock.patch("app.main.has_internet_connection")
    #       as mock_has_internet_connection,
    #       mock.patch("app.main.valid_google_url")
    #       as mock_valid_google_url):

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    can_access_google_page("")

    assert can_access_google_page("") == "Not accessible"
