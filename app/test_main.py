from unittest import mock

from app.main import valid_google_url, has_internet_connection, can_access_google_page

def test_valid_url():
    with mock.patch("app.main.valid_google_url", return_value=True) as mocked_valid_google_url:
        assert mocked_valid_google_url()

def test_has_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_has_internet_connection:
        assert mocked_has_internet_connection()
def test_should_access_google_page():
    with mock.patch("app.main.can_access_google_connectioin") as mocked_can_access_google_connection:
        result = mocked_can_access_google_connection("https://www.google.com/")
        assert result == "Accessible"
