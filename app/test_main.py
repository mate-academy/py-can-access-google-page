import pytest
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "url, mock_valid_google_url_return, mock_has_internet_connection_return, expected_result",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.google.com", False, True, "Not accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("http://www.google.com", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(mocker, url, mock_valid_google_url_return, mock_has_internet_connection_return, expected_result):
    mocker.patch('app.main.valid_google_url', return_value=mock_valid_google_url_return)
    mocker.patch('app.main.has_internet_connection', return_value=mock_has_internet_connection_return)
    result = can_access_google_page(url)
    assert result == expected_result
