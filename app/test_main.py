import pytest
from typing import Callable
from unittest.mock import patch

from app.main import can_access_google_page


url = "http://www.google.com"


@pytest.fixture
def mock_valid_url() -> None:
    with patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture
def mock_internet_available() -> None:
    with patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


def test_is_accessible(
        mock_valid_url: Callable,
        mock_internet_available: None
) -> None:
    mock_valid_url.return_value = True
    mock_internet_available.return_value = True
    assert can_access_google_page(url) == "Accessible"


def test_is_not_accessible_because_of_connection(
        mock_valid_url: Callable,
        mock_internet_available: Callable
) -> None:
    mock_valid_url.return_value = False
    mock_internet_available.return_value = True
    assert can_access_google_page(url) == "Not accessible",\
        "Url is not valid."


def test_is_not_accessible_because_of_url(
        mock_valid_url: Callable,
        mock_internet_available: Callable
) -> None:
    mock_valid_url.return_value = True
    mock_internet_available.return_value = False
    assert can_access_google_page(url) == "Not accessible",\
        "Fix your internet connection!"


def test_is_not_accessible_because_of_url_and_internet_conection(
        mock_valid_url: Callable,
        mock_internet_available: Callable
) -> None:
    mock_valid_url.return_value = False
    mock_internet_available.return_value = False
    assert can_access_google_page(url) == "Not accessible",\
        "Url is not valid and there is no internet connection"
