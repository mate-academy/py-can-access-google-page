from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_url: Any,
    mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_no_internet(
    mock_valid_url: Any,
    mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_invalid_url(
    mock_valid_url: Any,
    mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("https://invalid.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_not_accessible_both_false(
    mock_valid_url: Any,
    mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    assert can_access_google_page("https://invalid.com") == "Not accessible"
