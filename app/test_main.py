from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_all_true_can_access_google_page(mock_connection, mock_url) -> None:
    mock_connection.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_not_true_can_access_google_page(mock_connection, mock_url) -> None:
    mock_connection.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection_not_true_can_access_google_page(mock_connection, mock_url) -> None:
    mock_connection.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"