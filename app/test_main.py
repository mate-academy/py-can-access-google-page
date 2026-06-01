from unittest import mock
from app.main import can_access_google_page

@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_both_conditions_satisfied(mock_connection, mock_valid_url) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page(url='https://www.google.com')

    assert result == "Accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_no_internet_connection(mock_connection, mock_valid_url) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page(url='https://www.google.com')

    assert result == "Not accessible"


@mock.patch('app.main.has_internet_connection')
@mock.patch('app.main.valid_google_url')
def test_invalid_url(mock_connection, mock_valid_url) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page(url='https://www.google.com')

    assert result == "Not accessible"