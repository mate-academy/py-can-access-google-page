from typing import Generator
from unittest import mock

import pytest

from app import main

from .main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Generator:
    with mock.patch("app.main.valid_google_url") as val_url:
        val_url.return_value = True
        yield val_url


@pytest.fixture()
def mock_has_internet_connection() -> Generator:
    with mock.patch("app.main.has_internet_connection") as has_conn:
        has_conn.return_value = True
        yield has_conn


def test_valid_url_and_connection_returns_accessible(
    mock_valid_google_url: callable, mock_has_internet_connection: callable
) -> None:
    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_functions_were_called(
    mock_valid_google_url: callable, mock_has_internet_connection: callable
) -> None:
    can_access_google_page("https://www.google.com/")
    mock_valid_google_url.assert_called_once()
    mock_has_internet_connection.assert_called_once()


def test_no_internet_connection(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: True)
    monkeypatch.setattr(main, "has_internet_connection", lambda: False)
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


def test_invalid_google_url(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: False)
    monkeypatch.setattr(main, "has_internet_connection", lambda: True)
    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )
