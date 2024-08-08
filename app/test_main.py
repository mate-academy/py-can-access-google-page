from typing import Callable

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google() -> Callable:
    with mock.patch("app.main.valid_google_url") as valid_mock:
        yield valid_mock


@pytest.fixture
def mock_has_internet() -> Callable:
    with mock.patch("app.main.has_internet_connection") as internet_mock:
        yield internet_mock


def test_if_can_access_google_page_works_correctly(mock_valid_google, mock_has_internet):
    mock_valid_google.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("some_url") == "Accessible"

    mock_valid_google.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("some_url") == "Not accessible"

    mock_valid_google.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("some_url") == "Not accessible"

    mock_valid_google.return_value = False
    mock_has_internet.return_value = False
    assert can_access_google_page("some_url") == "Not accessible"
