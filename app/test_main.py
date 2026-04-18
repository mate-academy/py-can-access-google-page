from unittest.mock import patch, MagicMock
import app.main as main_module
from app.main import valid_google_url, has_internet_connection


@patch("app.main.requests.get")
def test_valid_url_returns_true(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 200
    assert valid_google_url("https://google.com") is True


@patch("app.main.requests.get")
def test_invalid_url_returns_false(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 404
    assert valid_google_url("https://google.com") is False


@patch("app.main.datetime.datetime")
def test_if_current_time_is_between_6_and_23(mock_datetime: MagicMock) -> None:
    mock_datetime.now.return_value.hour = 10
    assert has_internet_connection() is True


@patch("app.main.datetime.datetime")
def test_if_current_time_is_outside_working_hours(
    mock_datetime: MagicMock
) -> None:
    mock_datetime.now.return_value.hour = 2
    assert has_internet_connection() is False


@patch("app.main.requests.get")
@patch("app.main.datetime.datetime")
def test_can_access_google_page_accessible(
    mock_datetime: MagicMock,
    mock_get: MagicMock
) -> None:
    mock_datetime.now.return_value.hour = 12
    mock_get.return_value.status_code = 200
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.requests.get")
@patch("app.main.datetime.datetime")
def test_cannot_access_if_only_connection_is_true(
    mock_datetime: MagicMock,
    mock_get: MagicMock
) -> None:
    mock_datetime.now.return_value.hour = 12
    mock_get.return_value.status_code = 404
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.requests.get")
@patch("app.main.datetime.datetime")
def test_cannot_access_if_only_valid_url_is_true(
    mock_datetime: MagicMock,
    mock_get: MagicMock
) -> None:
    mock_datetime.now.return_value.hour = 3
    mock_get.return_value.status_code = 200
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.requests.get")
@patch("app.main.datetime.datetime")
def test_cannot_access_if_both_false(
    mock_datetime: MagicMock,
    mock_get: MagicMock
) -> None:
    mock_datetime.now.return_value.hour = 1
    mock_get.return_value.status_code = 404
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"
