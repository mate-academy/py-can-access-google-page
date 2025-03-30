from unittest import mock
import pytest
from .main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, can_access_google",
    [
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, True, "Not accessible"),

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock,
        mock_has_internet_connection: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        can_access_google: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("https://google.com") == can_access_google
