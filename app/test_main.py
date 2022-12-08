from unittest import mock
from .main import can_access_google_page
import pytest


@pytest.fixture()
def mock_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_function_accesses_website(
        mock_valid_url: mock,
        mock_connection: mock) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("Some URL") == "Accessible"


def test_function_not_accesses_website_when_no_connection(
        mock_valid_url: mock,
        mock_connection: mock) -> None:
    mock_valid_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("Some URL") == "Not accessible"


def test_function_not_accesses_website_if_url_invalid(
        mock_valid_url: mock,
        mock_connection: mock) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("Some URL") == "Not accessible"


def test_function_not_accesses_website_if_both_false(
        mock_valid_url: mock,
        mock_connection: mock) -> None:
    mock_valid_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("Some URL") == "Not accessible"
