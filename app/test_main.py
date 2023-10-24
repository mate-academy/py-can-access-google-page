from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, get_access",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_valid_url_and_internet_connection(
        valid_url: bool,
        connection: bool,
        get_access: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url, \
            mock.patch("app.main.has_internet_connection") as mock_connection:
        mock_url.return_value = valid_url
        mock_connection.return_value = connection
        assert can_access_google_page("https://www.google.com") == get_access
