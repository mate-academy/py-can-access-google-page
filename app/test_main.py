import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, access_page",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
def test_valid_url_and_connection_exists(
        valid_url: bool,
        internet_connection: bool,
        access_page: str
) -> None:
    with (patch("app.main.valid_google_url") as mocked_url_check,
         patch("app.main.has_internet_connection") as mocked_internet_check):
        mocked_url_check.return_value = valid_url
        mocked_internet_check.return_value = internet_connection
        assert can_access_google_page("https://www.google.com") == access_page
