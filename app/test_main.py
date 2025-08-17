from unittest.mock import patch, MagicMock

import pytest

from app.main import (can_access_google_page,
                      valid_google_url,
                      has_internet_connection)


@pytest.mark.parametrize(
    "url",
    [
        "https://mate.academy/",
        "https://www.instagram.com/",
        "https://www.youtube.com/",
    ]
)
def test_valid_url(url: str) -> None:
    assert can_access_google_page(url) == "Accessible"


@patch("app.main.requests.get")
def test_valid_google_url_ok(mock_get: MagicMock) -> None:
    mock_get.return_value = MagicMock(status_code=200)
    assert valid_google_url("https://google.com") is True


@patch("app.main.requests.get")
def test_valid_google_url_fail(mock_get: MagicMock) -> None:
    mock_get.return_value = MagicMock(status_code=404)
    assert valid_google_url("https://google.com") is False


@patch("app.main.datetime")
def test_has_internet_connection_daytime(mock_datetime: MagicMock) -> None:
    mock_datetime.datetime.now.return_value.hour = 12
    assert has_internet_connection() is True


@patch("app.main.datetime")
def test_has_internet_connection_night(mock_datetime: MagicMock) -> None:
    mock_datetime.datetime.now.return_value.hour = 2
    assert has_internet_connection() is False


@patch("app.main.datetime")
def test_has_internet_connection_day(mock_datetime: MagicMock) -> None:
    mock_datetime.datetime.now.return_value.hour = 12
    assert has_internet_connection() is True


@patch("app.main.datetime")
def test_has_internet_connection_nighttime(mock_datetime: MagicMock) -> None:
    mock_datetime.datetime.now.return_value.hour = 2
    assert has_internet_connection() is False


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_ok(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_invalid_url(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://wrong.com") == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet(
        mock_conn: MagicMock,
        mock_valid: MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
