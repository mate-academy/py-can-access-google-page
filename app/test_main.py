from datetime import datetime
from unittest import mock
from app import main as app


def test_can_access_if_url_valid_and_has_connection() -> None:
    with (
        mock.patch("app.main.datetime") as mock_datetime,
        mock.patch("app.main.requests") as mock_requests,
    ):
        mock_datetime.datetime.now.return_value = datetime(
            2026, 12, 1, 7, 0, 0)
        mock_requests.get.return_value.status_code = 200

        assert app.can_access_google_page(
            "https://google.com.ua") == "Accessible"


def test_can_access_if_url_valid_and_has_not_connection() -> None:
    with (
        mock.patch("app.main.datetime") as mock_datetime,
        mock.patch("app.main.requests") as mock_requests,
    ):
        mock_datetime.datetime.now.return_value = datetime(
            2026, 12, 1, 5, 0, 0)
        mock_requests.get.return_value.status_code = 200

        assert app.can_access_google_page(
            "https://google.com.ua") == "Not accessible"


def test_can_access_if_url_not_valid_and_has_connection() -> None:
    with (
        mock.patch("app.main.datetime") as mock_datetime,
        mock.patch("app.main.requests") as mock_requests,
    ):
        mock_datetime.datetime.now.return_value = datetime(
            2026, 12, 1, 7, 0, 0)
        mock_requests.get.return_value.status_code = 404

        assert app.can_access_google_page(
            "https://google.com.ua") == "Not accessible"
