from unittest import mock
import requests
from app.main import can_access_google_page


@mock.patch("app.main.requests.get")
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists_returns_accessible(
        mock_valid_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        mock_get: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.requests.get")
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_invalid_url_returns_not_accessible(
        mock_valid_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        mock_get: mock.MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    assert (can_access_google_page
            ("https://invalid-url.com") == "Not accessible")
    mock_get.assert_not_called()


@mock.patch("app.main.requests.get")
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_no_internet_connection_time_returns_not_accessible(
        mock_valid_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        mock_get: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_get.assert_not_called()


@mock.patch("app.main.requests.get")
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_url_valid_but_request_fails_returns_not_accessible(
        mock_valid_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        mock_get: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    mock_get.side_effect = requests.RequestException

    assert can_access_google_page("https://google.com") == "Not accessible"
