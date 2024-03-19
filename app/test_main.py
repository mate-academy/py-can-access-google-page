from unittest.mock import patch
from app.main import can_access_google_page
import datetime


def test_can_access_google_page() -> None:
    url = "http://www.google.com"
    current_time = datetime.datetime.now()
    with patch("app.main.requests.get") as mock_get:
        with patch(
                "app.main.has_internet_connection",
                return_value=True
        ) as mock_internet:
            can_access_google_page(url)
            mock_get.assert_called_once_with(url)
            mock_internet.assert_called_once_with(current_time)
