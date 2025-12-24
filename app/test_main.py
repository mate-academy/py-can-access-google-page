import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_test_valid_url:
        yield mock_test_valid_url


def test_func_valid_google_url_was_called(mock_valid_url: Callable) -> None:
    can_access_google_page("http://google.com")
    mock_valid_url.assert_called_once_with("http://google.com")


@pytest.fixture()
def mock_has_internet_connection() -> None:
    path = "app.main.has_internet_connection"
    with mock.patch(path) as mock_internet_connection:
        yield mock_internet_connection


def test_func_has_internet_connection_was_called(
        mock_has_internet_connection: Callable
) -> None:
    can_access_google_page("http://google.com")
    mock_has_internet_connection.assert_called_once()


def test_if_valid_url_and_has_internet_connection_return_accessible_(
        mock_valid_url: Callable,
        mock_has_internet_connection: Callable
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"


def test_if_invalid_url_and_has_internet_connection_return_not_accessible_(
        mock_valid_url: Callable,
        mock_has_internet_connection: Callable
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"


def test_if_valid_url_and_has_not_internet_connection_return_not_accessible_(
        mock_valid_url: Callable,
        mock_has_internet_connection: Callable
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"


def test_raises_value_error_if_url_empty() -> None:
    with pytest.raises(ValueError):
        can_access_google_page("")


def test_raises_type_error_if_no_params() -> None:
    with pytest.raises(TypeError):
        can_access_google_page()
