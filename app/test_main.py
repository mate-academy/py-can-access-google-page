from app.main import can_access_google_page

from unittest.mock import patch

from typing import Callable


@patch(
    "app.main.has_internet_connection",
    return_value=True
)
@patch(
    "app.main.valid_google_url",
    return_value=True
)
def test_accessible_google_page(
    has_internet_connection_mock: Callable,
    valid_google_url_mock: Callable
) -> None:
    assert can_access_google_page("google.com") == "Accessible"


@patch(
    "app.main.has_internet_connection",
    return_value=False
)
@patch(
    "app.main.valid_google_url",
    return_value=True
)
def test_not_accessible_google_page_when_connection_return_false(
    has_internet_connection_mock: Callable,
    valid_google_url_mock: Callable
) -> None:
    assert can_access_google_page("google.com") == "Not accessible"


@patch(
    "app.main.has_internet_connection",
    return_value=True
)
@patch(
    "app.main.valid_google_url",
    return_value=False
)
def test_not_accessible_google_page_when_valid_return_false(
    has_internet_connection_mock: Callable,
    valid_google_url_mock: Callable
) -> None:
    assert can_access_google_page("google.com") == "Not accessible"
