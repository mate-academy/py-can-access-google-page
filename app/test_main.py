from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page("https://www.google.com")\
                   == "Not accessible"

        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page("https://www.google.com")\
                   == "Accessible"

        with patch("app.main.valid_google_url", return_value=False):
            assert can_access_google_page("https://invalidurl.com")\
                   == "Not accessible"
