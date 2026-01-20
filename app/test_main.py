from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "url_check, internet_check, access_check",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_check_accessibility(
        mocked_url: bool,
        mocked_internet: bool,
        url_check: bool,
        internet_check: bool,
        access_check: str
) -> None:
    mocked_url.return_value = url_check
    mocked_internet.return_value = internet_check
    assert can_access_google_page("https://www.google.com") == access_check
