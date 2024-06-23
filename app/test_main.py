from unittest import mock
from app.main import can_access_google_page


def mocked_valid_google_url(url: str) -> bool:
    response = mock.patch("requests.get")
    response_status_code = mock.patch("response.status_code")
    if response_status_code == 200:
        return True
    else:
        return False


def mocked_has_internet_connection() -> bool:
    current_time = mock.patch("datetime.datetime.now.hour")
    return True if current_time in range(6, 23) else False


def test_can_access_google_page():
    assert can_access_google_page('https://www.google.com') == "Accessible"
