import pytest
from unittest.mock import Mock, patch

from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> None:
    with patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture
def mock_has_internet_connection() -> None:
    with patch("app.main.has_internet_connection") as mock_internet_connection:
        yield mock_internet_connection


@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        ("https://www.google.com", True, "Accessible"),
        ("https://www.google.com", False, "Not accessible"),
        ("https://www.invalidurl.com", True, "Not accessible"),
        ("https://www.invalidurl.com", False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        valid_url: str,
        has_internet: bool,
        expected_result: str,
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = not valid_url.endswith("invalidurl.com")
    mock_has_internet_connection.return_value = has_internet

    assert can_access_google_page(valid_url) == expected_result
