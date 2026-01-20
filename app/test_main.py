from unittest import mock
from app.main import can_access_google_page


@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_valid_url_and_connection_exists(mock_internet: bool, mock_valid_url: bool) \
        -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    assert (can_access_google_page('https://www.google.com')
            == 'Accessible')

    mock_internet.return_value = False
    mock_valid_url.return_value = True
    assert (can_access_google_page('https://www.google.com')
            == 'Not accessible')

    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert (can_access_google_page('https://invalid-url.com')
            == 'Not accessible')

    mock_internet.return_value = False
    mock_valid_url.return_value = False
    assert (can_access_google_page('https://invalid-url.com')
            == 'Not accessible')
