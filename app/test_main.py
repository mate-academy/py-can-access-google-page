from unittest import mock
from datetime import datetime
from app.main import can_access_google_page


def test_can_access_google_page_valid_url_and_connection() -> None:
    with mock.patch(
        "app.main.valid_google_url",
        return_value=True
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=True
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_can_access_google_page_invalid_url() -> None:
    with mock.patch(
        "app.main.valid_google_url",
        return_value=False
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=True
    ):
        result = can_access_google_page("https://www.invalidgoogle.com")
        assert result == "Not accessible"


def test_can_access_google_page_no_internet_connection() -> None:
    with mock.patch(
        "app.main.valid_google_url",
        return_value=True
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=False
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"


def test_can_access_google_page_invalid_url_and_no_internet_connection() \
        -> None:
    with mock.patch(
        "app.main.valid_google_url",
        return_value=False
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=False
    ):
        result = can_access_google_page("https://www.invalidgoogle.com")
        assert result == "Not accessible"


def test_can_access_google_page_internet_outside_time_range() -> None:
    with mock.patch(
        "app.main.valid_google_url",
        return_value=True
    ), mock.patch(
        "app.main.has_internet_connection",
        return_value=False
    ), mock.patch(
        "app.main.datetime"
    ) as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 10, 21, 23, 0, 0)
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
