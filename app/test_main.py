from app.main import can_access_google_page
from typing import Any


def test_can_access_google_page_accessible(mocker: Any) -> None:
    """Test that the function returns "Accessible"
    when URL is valid and internet is available."""
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_invalid_url(mocker: Any) -> None:
    """Test that the function returns "Not accessible" when URL is invalid."""
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=True)
    assert can_access_google_page("https://example.com") == "Not accessible"


def test_can_access_google_page_no_internet(mocker: Any) -> None:
    """Test that the function returns "Not accessible"
    when there is no internet connection."""
    mocker.patch("app.main.valid_google_url", return_value=True)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_both_conditions_fail(mocker: Any) -> None:
    """Test that the function returns "Not accessible"
    when both URL is invalid and no internet."""
    mocker.patch("app.main.valid_google_url", return_value=False)
    mocker.patch("app.main.has_internet_connection", return_value=False)
    assert can_access_google_page("https://example.com") == "Not accessible"
