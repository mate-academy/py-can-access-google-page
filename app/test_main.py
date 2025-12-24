from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_url: bool,
        mock_connection: bool) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page(
        "https://mate.academy/learn/python-core/python-core-testing-in-details"
    ) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_only_valid_url_exists(mock_url: bool, mock_connection: bool) -> None:
    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page(
        "https://mate.academy/learn/python-core/python-core-testing-in-details"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_only_connection_exists(mock_url: bool, mock_connection: bool) -> None:
    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page(
        "https://mate.academy/learn/python-core/python-core-testing-in-details"
    ) == "Not accessible"
