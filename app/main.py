import requests
from datetime import datetime

def valid_google_url(url: str) -> bool:
    valid_urls = ["https://www.google.com", "http://www.google.com"]
    return url in valid_urls

def has_internet_connection() -> bool:
    current_time = datetime.now().time()
    start_time = datetime.strptime("06:00:00", "%H:%M:%S").time()
    end_time = datetime.strptime("22:59:59", "%H:%M:%S").time()
    return start_time <= current_time <= end_time

def can_access_google_page(url: str) -> str:
    if valid_google_url(url) and has_internet_connection():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return "Accessible"
        except requests.RequestException:
            pass
    return "Not accessible"
