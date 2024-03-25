from unittest.mock import patch, Mock
import pytest
from app.main import can_access_google_page, valid_google_url


@pytest.fixture()
def mock_valid_google() -> Mock:
    with patch("app.main.valid_google_url") as valid_google:
        yield valid_google


@pytest.fixture()
def mock_has_internet_connection() -> Mock:
    with patch("app.main.has_internet_connection") as connection:
        yield connection


def test_access_google_true(mock_valid_google: Mock,
                            mock_has_internet_connection: Mock) -> None:
    mock_valid_google.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"


def test_access_google_false_true(mock_valid_google: Mock,
                                  mock_has_internet_connection: Mock) -> None:
    mock_valid_google.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


def test_access_google_true_false(mock_valid_google: Mock,
                                  mock_has_internet_connection: Mock) -> None:
    mock_valid_google.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", True),  # Valid Google URL
    ("https://www.example.com", False),  # Non-Google URL
    ("invalid_url", False),  # Invalid URL
])
def test_valid_google_url(url: str, expected_result: bool) -> None:
    assert valid_google_url(url) == expected_result
