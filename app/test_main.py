from __future__ import annotations
from unittest import mock
import pytest
import requests

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_morning_internet(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("Accessible") == "Accessible"


def test_night_internet(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    response = requests.get("https://www.google.com/")
    response_result = True if response.status_code == 200 else False
    mock_valid_google_url.return_value = response_result
    mock_internet_connection.return_value = False
    assert can_access_google_page("Not accessible") == "Not accessible"


def test_valid_google_url_badly(
        mock_valid_google_url: callable,
        mock_internet_connection: callable
) -> None:

    response = requests.get("https://www.google.com/gf")
    response_result = True if response.status_code == 200 else False
    mock_valid_google_url.return_value = response_result
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/gf") == \
           "Not accessible"
