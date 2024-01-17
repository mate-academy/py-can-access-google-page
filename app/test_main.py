from __future__ import annotations

import pytest

from unittest.mock import patch, Mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> Mock:
    with patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mock_has_internet_connection() -> Mock:
    with patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "url, is_url_valid, has_connection, response",
    [
        ("https://mate.academy/", False, True, "Not accessible"),
        ("https://mate.academy/", True, False, "Not accessible"),
        ("https://mate.academy/", True, True, "Accessible"),
        ("https://mate.academy/", False, False, "Not accessible")
    ],
    ids=[
        "invalid_url_but_has_internet_connection",
        "no_internet_connection_but_valid_url",
        "can_access_google_page",
        "no_internet_connection_and_invalid_url"
    ]
)
def test_main_cases_for_can_access_google_page(
    url: str,
    is_url_valid: bool,
    has_connection: bool,
    response: str,
    mock_valid_google_url: Mock,
    mock_has_internet_connection: Mock
) -> None:
    mock_valid_google_url.return_value = is_url_valid
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page(url) == response
