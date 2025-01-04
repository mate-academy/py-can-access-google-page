import datetime
import requests

from unittest import mock

from app.main import valid_google_url, has_internet_connection


def test_valid_google_url(url: str) -> None:
    requests.get = mock.MagicMock()
    response = requests.get(url)
    assert response.status_code == 200


def test_has_internet_connection() -> None:
    datetime.datetime.now = mock.MagicMock()
    current_time = datetime.datetime.now()
    assert current_time.hour in range(6, 23)


def test_can_access_google_page(url: str) -> None:
    if has_internet_connection() and valid_google_url(url):
        assert "Accessible", "Not accessible"
