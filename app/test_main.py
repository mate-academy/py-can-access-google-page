from unittest import mock
from typing import Any

import app.main

google_url = "https://www.google.com"
invalid_url = "https://www.invalidurl.com"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_accessible(mock_valid_url: Any, mock_has_internet: Any) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert app.main.can_access_google_page(google_url) == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_due_to_invalid_url(
        mock_valid_url: Any,
        mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert app.main.can_access_google_page(invalid_url) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_due_to_no_internet_connection(
        mock_valid_url: Any,
        mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert app.main.can_access_google_page(google_url) == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_not_accessible_due_to_invalid_url_and_no_internet_connection(
        mock_valid_url: Any,
        mock_has_internet: Any
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert app.main.can_access_google_page(invalid_url) == "Not accessible"
