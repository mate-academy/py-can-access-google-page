from typing import Any
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_connection_valid_url(
        mock_valid_google_url: Any, mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_connection_valid_url(
        mock_valid_google_url: Any, mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_connection_not_valid_url(
        mock_valid_google_url: Any, mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_connection_not_valid_url(
        mock_valid_google_url: Any, mock_has_internet_connection: Any
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("") == "Not accessible"
