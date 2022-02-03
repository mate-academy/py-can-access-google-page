import time
import datetime


def valid_google_url(url):
    valid_urls = [
        "https://www.google.com"
        "google.com",
        "google.com.ua",
    ]
    time.sleep(5)
    return True if url in valid_urls else False


def has_internet_connection():
    current_time = datetime.datetime.now()
    return True if current_time.hour in range(6, 23) else False


def can_access_google_page(url):
    return "Accessible" if valid_google_url(url) and has_internet_connection() else "Not accessible"
