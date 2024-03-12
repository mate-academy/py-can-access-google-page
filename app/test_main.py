from typing import Any
from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_only_valid_google_url(
        mock_test_has_internet_connection: Any,
        mock_test_valid_google_url: Any
) -> None:
    mock_test_valid_google_url.return_value = True
    mock_test_has_internet_connection.return_value = False

    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_only_connection_exist(
        mock_test_has_internet_connection: Any,
        mock_test_valid_google_url: Any
) -> None:
    mock_test_valid_google_url.return_value = False
    mock_test_has_internet_connection.return_value = True

    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_no_connection_and_invalid_google_url(
        mock_test_has_internet_connection: Any,
        mock_test_valid_google_url: Any
) -> None:
    mock_test_valid_google_url.return_value = False
    mock_test_has_internet_connection.return_value = False

    assert can_access_google_page("some_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_when_connection_exist_and_valid_google_url(
        mock_test_has_internet_connection: Any,
        mock_test_valid_google_url: Any
) -> None:
    mock_test_valid_google_url.return_value = True
    mock_test_has_internet_connection.return_value = True

    assert can_access_google_page("some_url") == "Accessible"
