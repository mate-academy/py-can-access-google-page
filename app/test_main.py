import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_requests_get():
    with patch("app.main.requests.get") as mock_get:
        yield mock_get


@pytest.fixture
def mock_datetime_now():
    with patch("app.main.datetime.datetime") as mock_datetime:
        yield mock_datetime.now


def test_can_access_google_page_access_granted(
        mock_requests_get,
        mock_datetime_now):
    mock_requests_get.return_value.status_code = 200
    mock_datetime_now.return_value.hour = 12
    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


def test_can_access_google_page_no_internet_connection(
        mock_requests_get,
        mock_datetime_now):
    mock_datetime_now.return_value.hour = 2
    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


def test_can_access_google_page_invalid_url(
        mock_requests_get,
        mock_datetime_now):
    mock_requests_get.return_value.status_code = 404
    mock_datetime_now.return_value.hour = 12
    result = can_access_google_page("https://invalid-url.com")
    assert result == "Not accessible"
