from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.fixture()
def mock_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_if_all_false(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Invalid url. Page is not accessible."
    )


def test_cannot_access_if_no_internet_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Page is not accessible without internet connection."
    )


def test_if_all_true(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Accessible", (
        "Page is Accessible."
    )


def test_cannot_access_if_only_internet_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("www.google.com/") == "Not accessible", (
        "Page is not accessible. "
        "Invalid url and internet connection is down."
    )
