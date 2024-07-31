from typing import Callable
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def patch_inner_functions() -> Callable:
    with mock.patch("app.main.valid_google_url") as mocked_url, \
         mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_url, mocked_connection


def test_accesible_with_valid_url_and_internet_connection(
        patch_inner_functions: Callable
) -> None:
    mock_url, mock_connection = patch_inner_functions

    mock_url.return_value = True
    mock_connection.return_value = True

    assert can_access_google_page("https://www.google.com/") == "Accessible"


def test_not_accessible_without_valid_url(
        patch_inner_functions: Callable
) -> None:
    mock_url, mock_connection = patch_inner_functions

    mock_url.return_value = False
    mock_connection.return_value = True

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


def test_not_accessible_without_connection(
        patch_inner_functions: Callable
) -> None:
    mock_url, mock_connection = patch_inner_functions

    mock_url.return_value = True
    mock_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )


def test_not_accessible_without_valid_url_and_connection(
        patch_inner_functions: Callable
) -> None:
    mock_url, mock_connection = patch_inner_functions

    mock_url.return_value = False
    mock_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/") == "Not accessible"
    )
