from typing import Callable
from unittest.mock import patch
from unittest.mock import MagicMock
from app.main import valid_google_url
from app.main import has_internet_connection
from app.main import can_access_google_page


@patch("app.main.datetime")
def test_has_internet_connection(moke_date_time: MagicMock) -> None:
    moke_date_time.datetime.now().hour = 7
    assert has_internet_connection()
    moke_date_time.datetime.now().hour = 24
    assert not has_internet_connection()


@patch("app.main.requests.get")
def test_valid_google_url(mock_get: MagicMock) -> None:
    url = "https://"
    mock_get.return_value.status_code = 200
    assert valid_google_url(url)
    mock_get.return_value.status_code = 404
    assert not valid_google_url(url)


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: Callable,
        mock_valid_google_url: Callable
) -> None:
    url = "https://"
    mock_has_internet_connection.return_value = False
    assert can_access_google_page(url) == "Not accessible"
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page(url) == "Accessible"
