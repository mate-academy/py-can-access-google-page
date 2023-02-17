from unittest import mock
import pytest
from .main import can_access_google_page
@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection,  access",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")

    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_internet_access(
        mock_valid_google_url,
        mock_has_internet_connection,
        valid_google_url,
        has_internet_connection,
        access

) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    # mock_has_internet_connection.return_value, mock_valid_google_url.return_value
    assert can_access_google_page("https://google.com") == access




