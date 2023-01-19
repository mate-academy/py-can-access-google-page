from __future__ import annotations
from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_internet_work_and_url_ok(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") ==\
           "Accessible"


def test_internet_not_work_url_ok(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"


def test_internet_work_and_url_not_valid_values(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"


def test_internet_not_work_and_url_not_valid_values(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com/") ==\
           "Not accessible"
