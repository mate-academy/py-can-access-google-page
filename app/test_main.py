import pytest
from unittest import mock
from app.main import can_access_google_page

@pytest.fixture
def mocks():
    with mock.patch("app.main.has_internet_connection") as mock_inet, \
         mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_inet, mock_url

def test_accessible(mocks):
    mock_inet, mock_url = mocks
    mock_inet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("mock") == "Accessible"

def test_no_internet(mocks):
    mock_inet, mock_url = mocks
    mock_inet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("mock") == "Not accessible"

def test_invalid_url(mocks):
    mock_inet, mock_url = mocks
    mock_inet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("mock") == "Not accessible"
