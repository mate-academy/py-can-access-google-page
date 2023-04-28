from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.fixture
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        yield mock_valid_google_url


@pytest.fixture
def mock_has_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_has_internet_connection:
        yield mock_has_internet_connection


@pytest.mark.parametrize(
    "url, result, valid_google_url, has_internet_connection",
    [
        ("https://www.google.com/", "Accessible", True, True),
        ("https://www.example.com/", "Not accessible", False, True),
        ("https://www.google.com/", "Not accessible", True, False),
        ("https://www.google.com/", "Not accessible", False, False)
    ]
)
def test_can_access_google_page_no_internet_connection(
        url: str,
        result: str,
        valid_google_url: bool,
        has_internet_connection: bool,
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page(url) == result
