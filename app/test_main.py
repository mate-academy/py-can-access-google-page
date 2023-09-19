from typing import Callable

import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def valid_google_url_mock() -> None:
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def has_internet_connection_mock() -> None:
    with patch("app.main.has_internet_connection") as mock:
        yield mock


def test_accessible(
        valid_google_url_mock: Callable,
        has_internet_connection_mock: Callable
) -> None:
    valid_google_url_mock.return_value = True
    has_internet_connection_mock.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_not_accessible_no_internet(
        valid_google_url_mock: Callable,
        has_internet_connection_mock: Callable
) -> None:
    valid_google_url_mock.return_value = True
    has_internet_connection_mock.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_not_accessible_invalid_url(valid_google_url_mock: Callable) -> None:
    valid_google_url_mock.return_value = False
    assert can_access_google_page("https://example.com") == "Not accessible"
