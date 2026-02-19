from app import main
from unittest.mock import patch


def test_accessible_on_valid_url_and_connection() -> None:
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


def test_not_accessible_on_invalid_url_and_no_connection() -> None:
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


def test_not_accessible_with_no_connection() -> None:
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


def test_not_accessible_with_invalid_url() -> None:
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
