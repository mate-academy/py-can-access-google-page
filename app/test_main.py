from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (patch("app.main.valid_google_url") as valid_url,
          patch("app.main.has_internet_connection") as has_connection):
        valid_url.return_value = True
        has_connection.return_value = True
        action = can_access_google_page("https://www.google.com/")

    assert action == "Accessible"


def test_can_not_access_google_page_if_only_connection() -> None:
    with (patch("app.main.valid_google_url") as valid_url,
          patch("app.main.has_internet_connection") as has_connection):
        valid_url.return_value = False
        has_connection.return_value = True
        action = can_access_google_page("www.some-random-website")

    assert action == "Not accessible"


def test_can_not_access_google_page_if_only_valid_url() -> None:
    with (patch("app.main.valid_google_url") as valid_url,
          patch("app.main.has_internet_connection") as has_connection):
        valid_url.return_value = True
        has_connection.return_value = False
        action = can_access_google_page("www.some-random-website")

    assert action == "Not accessible"
