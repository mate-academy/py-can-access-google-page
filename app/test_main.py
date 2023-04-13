import pytest

from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> Callable:
    with mock.patch("app.main.valid_google_url") as mock_valid_google:
        yield mock_valid_google


@pytest.fixture()
def mock_has_internet() -> Callable:
    with (
        mock.patch("app.main.has_internet_connection")
    ) as mock_has_internet_connection:
        yield mock_has_internet_connection


@pytest.mark.parametrize(
    "link, valid_url, has_internet, result",
    [
        ("google.com", True, True, "Accessible"),
        ("google.com/search", True, False, "Not accessible"),
        ("gogle.com", False, True, "Not accessible"),
        ("goglik.rom", False, False, "Not accessible")
    ],
    ids=[
        "test 1: function should return 'Accessible'",
        "test 2: function should return 'Not accessible'",
        "test 3: function should return 'Not accessible'",
        "test 4: function should return 'Not accessible'"
    ]
)
def test_can_access_google_page(
        link: str,
        valid_url: bool,
        has_internet: bool,
        result: str,
        mock_valid_url: Callable,
        mock_has_internet: Callable
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet.return_value = has_internet
    with mock_valid_url, mock_has_internet:
        assert (
            can_access_google_page(link) == result
        )
