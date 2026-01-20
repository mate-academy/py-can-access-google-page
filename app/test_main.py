import unittest.mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "google_url_status,internet_connection_status,result",
    [
        (
            True,
            False,
            "Not accessible"
        ),
        (
            False,
            True,
            "Not accessible"
        ),
        (
            False,
            False,
            "Not accessible"
        ),
        (
            True,
            True,
            "Accessible"
        )
    ]
)
@unittest.mock.patch("app.main.valid_google_url")
@unittest.mock.patch("app.main.has_internet_connection")
def test_access(has_internet_func: bool, valid_google_func: str,
                google_url_status: bool, internet_connection_status: bool,
                result: str
                ) -> None:

    has_internet_func.return_value = internet_connection_status
    valid_google_func.return_value = google_url_status
    assert can_access_google_page(
        "https://www.youtube.com/?app=desktop&gl=UA&hl=uk"
    ) == result
