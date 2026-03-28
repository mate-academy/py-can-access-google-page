from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (
        patch("app.main.valid_google_url", return_value=True),
        patch("app.main.has_internet_connection", return_value=True),
    ):
        assert can_access_google_page("google.com") == "Accessible"
