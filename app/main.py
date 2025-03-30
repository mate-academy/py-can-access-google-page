import datetime
import requests
from typing import Optional


def valid_google_url(url: str) -> bool:
    """
    Проверяет, является ли URL действительным для доступа к странице Google.

    :param url: URL для проверки.
    :return: True, если URL действителен, иначе False.
    """
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False


def has_internet_connection() -> bool:
    """
    Проверяет наличие интернет-соединения в заданное время (6:00 - 22:59).

    :return: True, если текущее время между 6:00 и 22:59, иначе False.
    """
    current_time = datetime.datetime.now()
    return 6 <= current_time.hour <= 22


def can_access_google_page(url: str) -> str:
    """
    Определяет, доступна ли страница Google по заданному URL.

    :param url: URL для проверки.
    :return: "Accessible", если страница доступна, иначе "Not accessible".
    """
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
