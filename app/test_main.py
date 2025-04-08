from unittest import mock
from app.main import can_access_google_page

url = "http://google.com/"

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_has_internet_false(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page(url)
    assert result == "Not accessible"

@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_not_valid_url(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page(url)
    assert result == "Not accessible"
