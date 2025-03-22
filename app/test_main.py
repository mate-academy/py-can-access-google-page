import pytest
from app.main import can_access_google_page
from unittest import  mock

@pytest.fixture()
def mocked_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mock_test_response:
        yield mock_test_response

@pytest.fixture()
def mocked_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_test_current_time:
        yield  mock_test_current_time

def test_can_access_google_page(mocked_valid_google_url, mocked_has_internet_connection):
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value =True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible", "Not accessible"

    mocked_valid_google_url.assert_called_with("https://www.google.com")
    mocked_has_internet_connection.assert_called()
# write your code here
