from datetime import datetime
from unittest import mock
from app import main as app


def test_can_access_to_google_page() -> None:
    with (
        mock.patch("app.main.datetime") as mock_datetime,
        mock.patch("app.main.requests") as mock_requests,
    ):
        mock_datetime.datetime.now.return_value = datetime(
            2026, 12, 1, 7, 0, 0
        )
        mock_requests.get.return_value.status_code = 200

        assert app.can_access_google_page(
            "https://google.com.ua") == "Accessible"
