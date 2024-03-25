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


@pytest.mark.parametrize(
    "valid_result, connect_result, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_access_google_page(mock_valid_google: Mock,
                            mock_has_internet_connection: Mock,
                            valid_result: bool, connect_result: bool,
                            expected_result: str) -> None:
    mock_valid_google.return_value = valid_result
    mock_has_internet_connection.return_value = connect_result

    assert can_access_google_page("url") == expected_result


@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", True),  # Valid Google URL
    ("https://www.example.com", False),  # Non-Google URL
    ("invalid_url", False),  # Invalid URL
])
def test_valid_google_url(url: str, expected_result: bool) -> None:
    assert valid_google_url(url) == expected_result
