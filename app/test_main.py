from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "google_url, internet_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        result: str,
        google_url: bool,
        internet_connection: bool
) -> None:
    with mock.patch("app.main.valid_google_url", return_value=google_url):
        with mock.patch(
                "app.main.has_internet_connection",
                return_value=internet_connection
        ):
            assert can_access_google_page("https://www.google.com") == result
