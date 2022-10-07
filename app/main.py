import datetime
from decimal import Decimal

import requests


def valid_google_url(url: str) -> bool:
    response = requests.get(url)
    return True if response.status_code == 200 else False


def has_internet_connection() -> bool:
    current_time = datetime.datetime.now()
    return True if current_time.hour in range(6, 23) else False


def can_access_google_page(url: str) -> str:
    if has_internet_connection() and valid_google_url(url):
        return "Accessible"
    else:
        return "Not accessible"


def odd_ones_out(numbers: list) -> list:
    d = {}

    for number in numbers:
        d[number] = d.get(number, 0) + 1


    for number in numbers[:]:
        print(number)
        if d[number] % 2:
            numbers.remove(number)

    return numbers
