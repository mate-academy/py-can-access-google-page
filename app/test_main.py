import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url():
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_both_func_work(mock_valid_url, mock_connection):
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("www.mate.academy") == "Accessible", (
        "the page is accessible if all working correct"
    )


def test_not_valid_url(mock_valid_url, mock_connection):
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("www.mate.academy") == "Not accessible", \
        "the page is inaccessible if the url is not correct"


def test_no_internet_connection(mock_valid_url, mock_connection):
    mock_valid_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("www.mate.academy") == "Not accessible", \
        "the page is inaccessible if the Internet is not working"


def test_both_func_do_not_work(mock_valid_url, mock_connection):
    mock_valid_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("www.mate.academy") == "Not accessible", \
        "the page is inaccessible if all is not working"
