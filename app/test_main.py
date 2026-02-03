import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_url_valid_and_internet_exists(
    mock_has_internet,
    mock_valid_url,
):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid(
    mock_has_internet,
    mock_valid_url,
):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("https://fake-google.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_has_internet,
    mock_valid_url,
):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_url_invalid_and_no_internet(
    mock_has_internet,
    mock_valid_url,
):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    result = can_access_google_page("invalid")

    assert result == "Not accessible"
