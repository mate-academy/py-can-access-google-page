from unittest import mock
import pytest
from .main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, site_access",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_check_google_url_access(
        mock_valid_google_url: mock,
        mock_has_internet_connection: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        site_access: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("google.com") == site_access
