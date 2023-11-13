from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, access_page",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: bool,
        mock_has_internet: bool,
        url: bool,
        internet_connection: bool,
        access_page: str
) -> None:
    mock_has_internet.return_value = internet_connection
    mock_valid_google_url.return_value = url

    assert can_access_google_page("https://www.google.com") == access_page
