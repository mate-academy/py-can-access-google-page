import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_functions():
    with patch("app.main.valid_google_url", return_value=True), \
         patch("app.main.has_internet_connection", return_value=True):
        yield


def test_can_access_google_page_valid_url_and_internet(mock_functions):
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


def test_car_access_google_page_valid_url_no_internet(mock_functions):
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


def test_can_access_google_page_invalid_url_with_internet(mock_functions):
    url = "https://example.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


def test_can_access_google_page_invalid_url_no_internet(mock_functions):
    url = "https://example.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


def test_can_access_google_page_invalid_url_not_internet(mock_functions):
    url = ""
    result = can_access_google_page(url)
    assert result == "Not accessible"
