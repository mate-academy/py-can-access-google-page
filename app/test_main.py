from app import main
from unittest.mock import patch


def test_can_access_google_page_if_time_and_url_correct() -> None:
    with patch(
        "app.main.has_internet_connection",
        return_value=True
    ), patch(
        "app.main.valid_google_url",
        return_value=True
    ):
        assert main.can_access_google_page(
            "https://www.google.com"
        ) == "Accessible"


def test_can_access_google_page_if_time_and_url_incorrect() -> None:
    with patch(
        "app.main.has_internet_connection",
        return_value=False
    ), patch(
        "app.main.valid_google_url",
        return_value=False
    ):
        assert main.can_access_google_page(
            "https://www.fake.com"
        ) == "Not accessible"


def test_can_access_google_page_if_time_incorrect() -> None:
    with patch(
        "app.main.has_internet_connection",
        return_value=False
    ), patch(
        "app.main.valid_google_url",
        return_value=True
    ):
        assert main.can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"


def test_can_access_google_page_if_url_incorrect() -> None:
    with patch(
        "app.main.has_internet_connection",
        return_value=True
    ), patch(
        "app.main.valid_google_url",
        return_value=False
    ):
        assert main.can_access_google_page(
            "https://www.fake.com"
        ) == "Not accessible"
