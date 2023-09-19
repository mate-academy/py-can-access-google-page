import pytest
from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


@pytest.fixture
def valid_google_url_mock() -> None:
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def has_internet_connection_mock() -> None:
    with patch("app.main.has_internet_connection") as mock:
        yield mock


@pytest.mark.parametrize(
    "valid_url, has_internet, url, expected_result",
    [
        (True, True, "https://www.google.com", "Accessible"),
        (True, False, "https://www.google.com", "Not accessible"),
        (False, False, "https://example.com", "Not accessible"),
        (False, True, "https://example.com", "Not accessible")
    ],
    ids=[
        "Accessible with Internet",
        "Not Accessible without Internet",
        "Not Accessible without Internet and Invalid URL",
        "Not Accessible with Invalid URL",
    ],
)
def test_can_access_google_page(
    valid_google_url_mock: Callable,
    has_internet_connection_mock: Callable,
    valid_url: bool,
    has_internet: bool,
    url: str,
    expected_result: str
) -> None:
    valid_google_url_mock.return_value = valid_url
    has_internet_connection_mock.return_value = has_internet
    assert can_access_google_page(url) == expected_result
