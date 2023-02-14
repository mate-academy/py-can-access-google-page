import pytest

from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_google_url() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_test_url:
        yield mock_test_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_test_connection:
        yield mock_test_connection


@pytest.mark.parametrize(
    "url, answer",
    [("www.googl.com", "Not accessible")]
)
def test_dont_have_internet_connection(
        mock_google_url: Callable,
        mock_internet_connection: Callable,
        url: str,
        answer: str
) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page(url) == answer


@pytest.mark.parametrize(
    "url, answer",
    [("www.googl.com", "Not accessible")]
)
def test_not_valid_googl_url(
        mock_google_url: Callable,
        mock_internet_connection: Callable,
        url: str,
        answer: str
) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page(url) == answer


@pytest.mark.parametrize(
    "url, answer",
    [("www.googl.com", "Not accessible")]
)
def test_dont_have_valid_googl_url_and_dont_have_internet_connection(
        mock_google_url: Callable,
        mock_internet_connection: Callable,
        url: str,
        answer: str
) -> None:
    mock_google_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page(url) == answer


@pytest.mark.parametrize(
    "url, answer",
    [("www.googl.com", "Accessible")]
)
def test_valid_googl_url_and_have_internet_connection(
        mock_google_url: Callable,
        mock_internet_connection: Callable,
        url: str,
        answer: str
) -> None:
    mock_google_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page(url) == answer
