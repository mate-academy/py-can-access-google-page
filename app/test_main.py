from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_url: Mock, mock_internet: Mock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_no_connection_exists(
        mock_valid_url: Mock, mock_internet: Mock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_connection_exists(
        mock_valid_url: Mock, mock_internet: Mock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection_exists(
        mock_valid_url: Mock, mock_internet: Mock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
