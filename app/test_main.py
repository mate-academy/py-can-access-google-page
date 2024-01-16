from __future__ import annotations

import pytest

from unittest.mock import patch, Mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Mock:
    with patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mock_has_internet_connection() -> Mock:
    with patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


def test_invalid_url_but_has_internet_connection(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_no_internet_connection_but_valid_url(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://mate.academy/") == "Accessible"
