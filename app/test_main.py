from unittest.mock import patch, Mock
from datetime import datetime

from app.main import can_access_google_page, has_internet_connection


# =========================
# Tests for can_access_google_page
# =========================

@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_returns_accessible_when_url_valid_and_internet_available(
    mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_returns_not_accessible_when_url_invalid(
    mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://not-google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_returns_not_accessible_when_no_internet(
    mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_returns_not_accessible_when_both_conditions_fail(
    mock_internet: Mock, mock_url: Mock
) -> None:
    result = can_access_google_page("https://bad.com")
    assert result == "Not accessible"


# =========================
# Tests for has_internet_connection (boundary time cases)
# =========================

@patch("app.main.datetime")
def test_connection_before_6_am(mock_datetime: Mock) -> None:
    mock_datetime.now.return_value = datetime(2024, 1, 1, 5, 59, 59)

    assert has_internet_connection() is False


@patch("app.main.datetime")
def test_connection_at_6_am(mock_datetime: Mock) -> None:
    mock_datetime.now.return_value = datetime(2024, 1, 1, 6, 0, 0)

    assert has_internet_connection() is True


@patch("app.main.datetime")
def test_connection_at_22_59_59(mock_datetime: Mock) -> None:
    mock_datetime.now.return_value = datetime(2024, 1, 1, 22, 59, 59)

    assert has_internet_connection() is True


@patch("app.main.datetime")
def test_connection_at_23_00_00(mock_datetime: Mock) -> None:
    mock_datetime.now.return_value = datetime(2024, 1, 1, 23, 0, 0)

    assert has_internet_connection() is False
