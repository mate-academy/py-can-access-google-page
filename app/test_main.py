from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exist(
        mock_has_connection: Any,
        mock_valid_google_url: Any
) -> None:
    mock_has_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_connection_exist(
        mock_has_connection: Any,
        mock_valid_google_url: Any
) -> None:
    mock_has_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page("Nothing") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_not_exists(
        mock_has_connection: Any,
        mock_valid_google_url: Any
) -> None:
    mock_has_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("Nothing") == "Not accessible"
