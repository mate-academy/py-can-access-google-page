from datetime import datetime

def has_internet_connection():
    """
    Проверяет наличие интернет-соединения, основываясь на текущем времени.
    Интернет-соединение доступно с 6:00:00 до 22:59:59.
    Возвращает:
        bool: True, если время в заданном диапазоне, иначе False.
    """
    current_time = datetime.now().time()
    start_time = datetime.strptime("06:00:00", "%H:%M:%S").time()
    end_time = datetime.strptime("22:59:59", "%H:%M:%S").time()
    return start_time <= current_time <= end_time

def valid_google_url(url):
    """
    Проверяет, является ли URL валидным Google-адресом.
    Аргументы:
        url (str): URL-адрес для проверки.
    Возвращает:
        bool: True, если URL валидный, иначе False.
    """
    return url.startswith("https://www.google.com")

def can_access_google_page(url):
    """
    Проверяет, доступна ли страница Google на основании интернет-соединения и валидности URL.
    Аргументы:
        url (str): URL-адрес для проверки.
    Возвращает:
        str: "Accessible", если страница доступна, иначе "Not accessible".
    """
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    return "Not accessible"
