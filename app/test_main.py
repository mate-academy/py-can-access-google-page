import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_google_deps():
    with patch("app.main.valid_google_url") as mock_url, \
         patch("app.main.has_internet_connection") as mock_conn:
        yield mock_url, mock_conn


def test_google_page_is_accessible_with_valid_url_and_connection(mock_google_deps):
    mock_valid_url, mock_has_connection = mock_google_deps
    mock_valid_url.return_value = True
    mock_has_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


def test_google_page_is_not_accessible_with_invalid_url(mock_google_deps):
    mock_valid_url, mock_has_connection = mock_google_deps
    mock_valid_url.return_value = False
    mock_has_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_google_page_is_not_accessible_without_connection(mock_google_deps):
    mock_valid_url, mock_has_connection = mock_google_deps
    mock_valid_url.return_value = True
    mock_has_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
