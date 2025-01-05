import datetime
import requests

from unittest import mock
from app.main import valid_google_url, has_internet_connection, can_access_google_page


@mock.patch("requests.get")
def test_valid_google_url(mock_get):
    # Імітуємо успішну відповідь від requests.get
    mock_get.return_value.status_code = 200
    url = "https://www.google.com"
    assert valid_google_url(url) is True


@mock.patch("datetime.datetime")
def test_has_internet_connection(mock_datetime):
    # Імітуємо поточний час
    mock_datetime.now.return_value = datetime.datetime(2024, 1, 5, 12, 0, 0)  # 12:00 (в робочому діапазоні)
    assert has_internet_connection() is True

    mock_datetime.now.return_value = datetime.datetime(2024, 1, 5, 1, 0, 0)  # 01:00 (поза робочим діапазоном)
    assert has_internet_connection() is False


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet, mock_valid_url):
    # Імітуємо, що інтернет доступний і URL правильний
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Accessible"

    # Імітуємо, що інтернет недоступний
    mock_internet.return_value = False
    assert can_access_google_page(url) == "Not accessible"

    # Імітуємо, що URL недійсний
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page(url) == "Not accessible"
