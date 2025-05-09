from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_can_access_google_page_accessible(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_can_access_google_page_not_valid_url(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_can_access_google_page_no_internet(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_can_access_google_page_not_valid_url_and_no_internet(
        mock_has_internet: MagicMock, mock_valid_url: MagicMock) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
